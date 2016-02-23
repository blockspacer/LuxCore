#include <string>
namespace slg { namespace ocl {
std::string KernelSource_mapping_funcs = 
"#line 2 \"mapping_funcs.cl\"\n"
"\n"
"/***************************************************************************\n"
" * Copyright 1998-2015 by authors (see AUTHORS.txt)                        *\n"
" *                                                                         *\n"
" *   This file is part of LuxRender.                                       *\n"
" *                                                                         *\n"
" * Licensed under the Apache License, Version 2.0 (the \"License\");         *\n"
" * you may not use this file except in compliance with the License.        *\n"
" * You may obtain a copy of the License at                                 *\n"
" *                                                                         *\n"
" *     http://www.apache.org/licenses/LICENSE-2.0                          *\n"
" *                                                                         *\n"
" * Unless required by applicable law or agreed to in writing, software     *\n"
" * distributed under the License is distributed on an \"AS IS\" BASIS,       *\n"
" * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.*\n"
" * See the License for the specific language governing permissions and     *\n"
" * limitations under the License.                                          *\n"
" ***************************************************************************/\n"
"\n"
"//------------------------------------------------------------------------------\n"
"// 2D mapping\n"
"//------------------------------------------------------------------------------\n"
"\n"
"float2 UVMapping2D_Map(__global const TextureMapping2D *mapping, __global HitPoint *hitPoint) {\n"
"	const float2 scale = VLOAD2F(&mapping->uvMapping2D.uScale);\n"
"	const float2 delta = VLOAD2F(&mapping->uvMapping2D.uDelta);\n"
"	const float2 uv = VLOAD2F(&hitPoint->uv.u);\n"
"\n"
"	return uv * scale + delta;\n"
"}\n"
"\n"
"float2 UVMapping2D_MapDuv(__global const TextureMapping2D *mapping, __global HitPoint *hitPoint, float2 *ds, float2 *dt) {\n"
"	(*ds).xy = VLOAD2F(&mapping->uvMapping2D.uScale);\n"
"	(*dt).xy = (float2)(0.f, (*ds).y);\n"
"	(*ds).y = 0.f;\n"
"	return UVMapping2D_Map(mapping, hitPoint);\n"
"}\n"
"\n"
"float2 TextureMapping2D_Map(__global const TextureMapping2D *mapping, __global HitPoint *hitPoint) {\n"
"	switch (mapping->type) {\n"
"		case UVMAPPING2D:\n"
"			return UVMapping2D_Map(mapping, hitPoint);\n"
"		default:\n"
"			return 0.f;\n"
"	}\n"
"}\n"
"\n"
"float2 TextureMapping2D_MapDuv(__global const TextureMapping2D *mapping, __global HitPoint *hitPoint, float2 *ds, float2 *dt) {\n"
"	switch (mapping->type) {\n"
"		case UVMAPPING2D:\n"
"			return UVMapping2D_MapDuv(mapping, hitPoint, ds, dt);\n"
"		default:\n"
"			return 0.f;\n"
"	}\n"
"}\n"
"\n"
"//------------------------------------------------------------------------------\n"
"// 3D mapping\n"
"//------------------------------------------------------------------------------\n"
"\n"
"float3 UVMapping3D_Map(__global const TextureMapping3D *mapping, __global HitPoint *hitPoint) {\n"
"	const float2 uv = VLOAD2F(&hitPoint->uv.u);\n"
"	return Transform_ApplyPoint(&mapping->worldToLocal, (float3)(uv.xy, 0.f));\n"
"}\n"
"\n"
"float3 GlobalMapping3D_Map(__global const TextureMapping3D *mapping, __global HitPoint *hitPoint) {\n"
"	const float3 p = VLOAD3F(&hitPoint->p.x);\n"
"	return Transform_ApplyPoint(&mapping->worldToLocal, p);\n"
"}\n"
"\n"
"float3 LocalMapping3D_Map(__global const TextureMapping3D *mapping, __global HitPoint *hitPoint) {\n"
"	const Matrix4x4 m = Matrix4x4_Mul(&mapping->worldToLocal.m, &hitPoint->worldToLocal);\n"
"	const float3 p = VLOAD3F(&hitPoint->p.x);\n"
"\n"
"	return Matrix4x4_ApplyPoint_Private(&m, p);\n"
"}\n"
"\n"
"float3 TextureMapping3D_Map(__global const TextureMapping3D *mapping, __global HitPoint *hitPoint) {\n"
"	switch (mapping->type) {\n"
"		case UVMAPPING3D:\n"
"			return UVMapping3D_Map(mapping, hitPoint);\n"
"		case GLOBALMAPPING3D:\n"
"			return GlobalMapping3D_Map(mapping, hitPoint);\n"
"		case LOCALMAPPING3D:\n"
"			return LocalMapping3D_Map(mapping, hitPoint);\n"
"		default:\n"
"			return 0.f;\n"
"	}\n"
"}\n"
; } }
