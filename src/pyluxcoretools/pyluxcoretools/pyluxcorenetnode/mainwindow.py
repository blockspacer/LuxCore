# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/david/projects/luxcorerender/LuxCore/src/pyluxcoretools/pyluxcoretools/pyluxcorenetnode/mainwindow.ui'
#
# Created: Sun Jun  3 10:43:14 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frameNodeConfig = QtGui.QFrame(self.centralwidget)
        self.frameNodeConfig.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameNodeConfig.setFrameShadow(QtGui.QFrame.Raised)
        self.frameNodeConfig.setObjectName("frameNodeConfig")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frameNodeConfig)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_7 = QtGui.QLabel(self.frameNodeConfig)
        self.label_7.setTextFormat(QtCore.Qt.RichText)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(self.frameNodeConfig)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(self.frameNodeConfig)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_4 = QtGui.QLabel(self.frameNodeConfig)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_3 = QtGui.QLabel(self.frameNodeConfig)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_5 = QtGui.QLabel(self.frameNodeConfig)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.lineEditIPAddress = QtGui.QLineEdit(self.frameNodeConfig)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditIPAddress.sizePolicy().hasHeightForWidth())
        self.lineEditIPAddress.setSizePolicy(sizePolicy)
        self.lineEditIPAddress.setMinimumSize(QtCore.QSize(250, 0))
        self.lineEditIPAddress.setInputMask("")
        self.lineEditIPAddress.setMaxLength(15)
        self.lineEditIPAddress.setObjectName("lineEditIPAddress")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditIPAddress)
        self.lineEditPort = QtGui.QLineEdit(self.frameNodeConfig)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditPort.sizePolicy().hasHeightForWidth())
        self.lineEditPort.setSizePolicy(sizePolicy)
        self.lineEditPort.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEditPort.setBaseSize(QtCore.QSize(0, 0))
        self.lineEditPort.setInputMask("")
        self.lineEditPort.setMaxLength(5)
        self.lineEditPort.setObjectName("lineEditPort")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEditPort)
        self.lineEditBroadcastAddress = QtGui.QLineEdit(self.frameNodeConfig)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditBroadcastAddress.sizePolicy().hasHeightForWidth())
        self.lineEditBroadcastAddress.setSizePolicy(sizePolicy)
        self.lineEditBroadcastAddress.setMinimumSize(QtCore.QSize(250, 0))
        self.lineEditBroadcastAddress.setObjectName("lineEditBroadcastAddress")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEditBroadcastAddress)
        self.lineEditBroadcastPeriod = QtGui.QLineEdit(self.frameNodeConfig)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditBroadcastPeriod.sizePolicy().hasHeightForWidth())
        self.lineEditBroadcastPeriod.setSizePolicy(sizePolicy)
        self.lineEditBroadcastPeriod.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEditBroadcastPeriod.setObjectName("lineEditBroadcastPeriod")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEditBroadcastPeriod)
        self.plainTextEditProps = QtGui.QPlainTextEdit(self.frameNodeConfig)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEditProps.sizePolicy().hasHeightForWidth())
        self.plainTextEditProps.setSizePolicy(sizePolicy)
        self.plainTextEditProps.setMinimumSize(QtCore.QSize(0, 50))
        self.plainTextEditProps.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.plainTextEditProps.setObjectName("plainTextEditProps")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.plainTextEditProps)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonResetConfiguration = QtGui.QPushButton(self.frameNodeConfig)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonResetConfiguration.sizePolicy().hasHeightForWidth())
        self.pushButtonResetConfiguration.setSizePolicy(sizePolicy)
        self.pushButtonResetConfiguration.setObjectName("pushButtonResetConfiguration")
        self.horizontalLayout_2.addWidget(self.pushButtonResetConfiguration)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.label_6 = QtGui.QLabel(self.frameNodeConfig)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.verticalLayout.addWidget(self.frameNodeConfig)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonStartNode = QtGui.QPushButton(self.centralwidget)
        self.pushButtonStartNode.setObjectName("pushButtonStartNode")
        self.horizontalLayout.addWidget(self.pushButtonStartNode)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonStopNode = QtGui.QPushButton(self.centralwidget)
        self.pushButtonStopNode.setEnabled(False)
        self.pushButtonStopNode.setObjectName("pushButtonStopNode")
        self.horizontalLayout.addWidget(self.pushButtonStopNode)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textEditLog = QtGui.QTextEdit(self.centralwidget)
        self.textEditLog.setUndoRedoEnabled(False)
        self.textEditLog.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.textEditLog.setReadOnly(True)
        self.textEditLog.setObjectName("textEditLog")
        self.verticalLayout.addWidget(self.textEditLog)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL("activated()"), MainWindow.clickedQuit)
        QtCore.QObject.connect(self.pushButtonResetConfiguration, QtCore.SIGNAL("clicked()"), MainWindow.clickedResetConfig)
        QtCore.QObject.connect(self.pushButtonStartNode, QtCore.SIGNAL("clicked()"), MainWindow.clickedStartNode)
        QtCore.QObject.connect(self.pushButtonStopNode, QtCore.SIGNAL("clicked(bool)"), MainWindow.clickedStopNode)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "PyLuxCore Tool NetNode", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "<B>Rendering Node Configuration<B>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Host name or IP address:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Port:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Broadcast period in secs:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Broadcast address:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Custom LuxCore properties:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonResetConfiguration.setText(QtGui.QApplication.translate("MainWindow", "Reset configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Note: just press \"Start node\" button to use the default configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonStartNode.setText(QtGui.QApplication.translate("MainWindow", "Start node", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonStopNode.setText(QtGui.QApplication.translate("MainWindow", "Stop node", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))

