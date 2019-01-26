/***************************************************************************
 * Copyright 1998-2018 by authors (see AUTHORS.txt)                        *
 *                                                                         *
 *   This file is part of LuxCoreRender.                                   *
 *                                                                         *
 * Licensed under the Apache License, Version 2.0 (the "License");         *
 * you may not use this file except in compliance with the License.        *
 * You may obtain a copy of the License at                                 *
 *                                                                         *
 *     http://www.apache.org/licenses/LICENSE-2.0                          *
 *                                                                         *
 * Unless required by applicable law or agreed to in writing, software     *
 * distributed under the License is distributed on an "AS IS" BASIS,       *
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.*
 * See the License for the specific language governing permissions and     *
 * limitations under the License.                                          *
 ***************************************************************************/

#ifndef _SLG_PHOTONGICACHE_H
#define	_SLG_PHOTONGICACHE_H

#include <vector>
#include <boost/atomic.hpp>

#include "luxrays/utils/properties.h"
#include "luxrays/utils/utils.h"

#include "slg/slg.h"
#include "slg/samplers/sampler.h"
#include "slg/bsdf/bsdf.h"
#include "slg/scene/scene.h"
#include "slg/engines/caches/photongi/pgicbvh.h"
#include "slg/engines/caches/photongi/pgicoctree.h"

namespace slg {

//------------------------------------------------------------------------------
// Photon Mapping Based GI cache
//------------------------------------------------------------------------------

struct GenericPhoton {
	GenericPhoton(const luxrays::Point &pt) : p(pt) {
	}

	luxrays::Point p;
};

struct VisibilityParticle : GenericPhoton {
	VisibilityParticle(const luxrays::Point &pt, const luxrays::Normal &nm) : GenericPhoton(pt),
		n(nm) {
	}

	luxrays::Normal n;
};
	
struct Photon : GenericPhoton {
	Photon(const luxrays::Point &pt, const luxrays::Vector &dir,
		const luxrays::Spectrum &a, const luxrays::Normal &n) : GenericPhoton(pt), d(dir),
		alpha(a), landingSurfaceNormal(n) {
	}

	luxrays::Vector d;
	luxrays::Spectrum alpha;
	luxrays::Normal landingSurfaceNormal;
};

struct RadiancePhoton : GenericPhoton {
	RadiancePhoton(const luxrays::Point &pt, const luxrays::Normal &nm,
		const luxrays::Spectrum &rad) : GenericPhoton(pt), n(nm), outgoingRadiance(rad) {
	}

	luxrays::Normal n;
	luxrays::Spectrum outgoingRadiance;
};

struct NearPhoton {
    NearPhoton(const GenericPhoton *p = nullptr, const float d2 = INFINITY) : photon(p),
			distance2(d2) {
	}

    bool operator<(const NearPhoton &p2) const {
        return (distance2 == p2.distance2) ?
            (photon < p2.photon) : (distance2 < p2.distance2);
    }

    const GenericPhoton *photon;
    float distance2;
};

//------------------------------------------------------------------------------
// PhotonGICache
//------------------------------------------------------------------------------

typedef enum {
	PGIC_DEBUG_SHOWDIRECT, PGIC_DEBUG_SHOWINDIRECT, PGIC_DEBUG_SHOWCAUSTIC, PGIC_DEBUG_NONE
} PhotonGIDebugType;

typedef enum {
	PGIC_SAMPLER_RANDOM, PGIC_SAMPLER_METROPOLIS
} PhotonGISamplerType;

class PhotonGICache {
public:
	PhotonGICache(const Scene *scn,
			const PhotonGISamplerType smplType,
			const bool visibilityEnabled,
			const float visibilityTargetHitRate,
			const u_int visibilityMaxSampleCount,
			const u_int maxPhotonTracedCount, const u_int maxPathDepth,
			const u_int entryMaxLookUpCount, const float entryRadius, const float entryNormalAngle,
			const bool directEnabled, u_int const maxDirectSize,
			const bool indirectEnabled, u_int const maxIndirectSize,
			const bool causticEnabled, u_int const maxCausticSize,
			const PhotonGIDebugType debugType);
	virtual ~PhotonGICache();

	PhotonGIDebugType GetDebugType() const { return debugType; }
	
	bool IsDirectEnabled() const { return directEnabled; }
	bool IsIndirectEnabled() const { return indirectEnabled; }
	bool IsCausticEnabled() const { return causticEnabled; }
	
	void Preprocess();

	luxrays::Spectrum GetAllRadiance(const BSDF &bsdf) const;
	luxrays::Spectrum GetDirectRadiance(const BSDF &bsdf) const;
	luxrays::Spectrum GetIndirectRadiance(const BSDF &bsdf) const;
	luxrays::Spectrum GetCausticRadiance(const BSDF &bsdf) const;

	static PhotonGISamplerType String2SamplerType(const std::string &type);
	static std::string SamplerType2String(const PhotonGISamplerType type);
	static PhotonGIDebugType String2DebugType(const std::string &type);
	static std::string DebugType2String(const PhotonGIDebugType type);

	static luxrays::Properties ToProperties(const luxrays::Properties &cfg);
	static const luxrays::Properties &GetDefaultProps();
	static PhotonGICache *FromProperties(const Scene *scn, const luxrays::Properties &cfg);

	friend class TracePhotonsThread;

private:
	void GenerateEyeRay(const Camera *camera, luxrays::Ray &eyeRay,
			PathVolumeInfo &volInfo, Sampler *sampler, SampleResult &sampleResult) const;
	void TraceVisibilityParticles();
	void TracePhotons(std::vector<Photon> &directPhotons, std::vector<Photon> &indirectPhotons,
			std::vector<Photon> &causticPhotons);
	void AddOutgoingRadiance(RadiancePhoton &radiacePhoton, const PGICPhotonBvh *photonsBVH,
			const u_int photonTracedCount) const;
	void FillRadiancePhotonData(RadiancePhoton &radiacePhoton);
	void FillRadiancePhotonsData();
	luxrays::Spectrum ProcessCacheEntries(const std::vector<NearPhoton> &entries,
			const u_int photonTracedCount, const float maxDistance2, const BSDF &bsdf) const;

	const Scene *scene;

	const PhotonGISamplerType samplerType;
	const bool visibilityEnabled;
	const float visibilityTargetHitRate;
	const u_int visibilityMaxSampleCount;
	const u_int maxPhotonTracedCount, maxPathDepth;
	const u_int entryMaxLookUpCount;
	const float entryRadius, entryRadius2, entryNormalAngle;
	const bool directEnabled, indirectEnabled, causticEnabled;
	const u_int maxDirectSize, maxIndirectSize, maxCausticSize;
	const PhotonGIDebugType debugType;
	
	boost::atomic<u_int> globalPhotonsCounter, globalDirectPhotonsTraced,
		globalIndirectPhotonsTraced, globalCausticPhotonsTraced,
		globalDirectSize, globalIndirectSize, globalCausticSize;
	SamplerSharedData *samplerSharedData;

	u_int directPhotonTracedCount, indirectPhotonTracedCount, causticPhotonTracedCount;

	// Visibility map
	std::vector<VisibilityParticle> visibilityParticles;
	PGCIOctree *visibilityParticlesOctree;

	// Photon maps
	std::vector<Photon> directPhotons, indirectPhotons, causticPhotons;
	PGICPhotonBvh *directPhotonsBVH, *indirectPhotonsBVH, *causticPhotonsBVH;
	
	// Radiance photon map
	std::vector<RadiancePhoton> radiancePhotons;
	PGICRadiancePhotonBvh *radiancePhotonsBVH;
};

}

#endif	/* _SLG_PHOTONGICACHE_H */
