# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'keyring.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_KeyRing(object):
    def setupUi(self, KeyRing):
        KeyRing.setObjectName("KeyRing")
        KeyRing.setWindowModality(QtCore.Qt.ApplicationModal)
        KeyRing.resize(770, 550)
        KeyRing.setMinimumSize(QtCore.QSize(770, 550))
        KeyRing.setMaximumSize(QtCore.QSize(770, 550))
        KeyRing.setAutoFillBackground(True)
        self.centralWidget = QtWidgets.QWidget(KeyRing)
        self.centralWidget.setObjectName("centralWidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralWidget)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(9, 9, 751, 451))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMaximumSize(QtCore.QSize(751, 16777215))
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setGridStyle(QtCore.Qt.DotLine)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.tableWidget.setItem(0, 0, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget.verticalHeader().setSortIndicatorShown(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.Save = QtWidgets.QPushButton(self.centralWidget)
        self.Save.setGeometry(QtCore.QRect(9, 470, 80, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Save.sizePolicy().hasHeightForWidth())
        self.Save.setSizePolicy(sizePolicy)
        self.Save.setObjectName("Save")
        self.Edit = QtWidgets.QPushButton(self.centralWidget)
        self.Edit.setGeometry(QtCore.QRect(90, 470, 80, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Edit.sizePolicy().hasHeightForWidth())
        self.Edit.setSizePolicy(sizePolicy)
        self.Edit.setObjectName("Edit")
        self.Delete = QtWidgets.QPushButton(self.centralWidget)
        self.Delete.setGeometry(QtCore.QRect(171, 470, 80, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Delete.sizePolicy().hasHeightForWidth())
        self.Delete.setSizePolicy(sizePolicy)
        self.Delete.setObjectName("Delete")
        self.statusLabel = QtWidgets.QLabel(self.centralWidget)
        self.statusLabel.setGeometry(QtCore.QRect(570, 470, 191, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusLabel.sizePolicy().hasHeightForWidth())
        self.statusLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.statusLabel.setFont(font)
        self.statusLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.statusLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.statusLabel.setObjectName("statusLabel")
        self.status = QtWidgets.QLabel(self.centralWidget)
        self.status.setGeometry(QtCore.QRect(508, 470, 59, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.status.sizePolicy().hasHeightForWidth())
        self.status.setSizePolicy(sizePolicy)
        self.status.setObjectName("status")
        KeyRing.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(KeyRing)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 770, 20))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuSettings = QtWidgets.QMenu(self.menuBar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuAbout = QtWidgets.QMenu(self.menuBar)
        self.menuAbout.setObjectName("menuAbout")
        KeyRing.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(KeyRing)
        self.statusBar.setObjectName("statusBar")
        KeyRing.setStatusBar(self.statusBar)
        self.actionSave = QtWidgets.QAction(KeyRing)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.setShortcut("CTRL+S")
        self.actionSettings = QtWidgets.QAction(KeyRing)
        self.actionSettings.setObjectName("actionSettings")
        self.actionExit = QtWidgets.QAction(KeyRing)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.setShortcut("CTRL+Q")
        self.actionGeneral_Settings = QtWidgets.QAction(KeyRing)
        self.actionGeneral_Settings.setObjectName("actionGeneral_Settings")
        self.actionAbout = QtWidgets.QAction(KeyRing)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout.setShortcut("F1")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuSettings.addAction(self.actionGeneral_Settings)
        self.menuAbout.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuSettings.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(KeyRing)
        QtCore.QMetaObject.connectSlotsByName(KeyRing)

    def retranslateUi(self, KeyRing):
        _translate = QtCore.QCoreApplication.translate
        KeyRing.setWindowTitle(_translate("KeyRing", "Leo Key Chain"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("KeyRing", "ID"))
        item.setToolTip(_translate("KeyRing", "<html><head/><body><p>Name of Service or Web Panel etc. that use this password.</p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("KeyRing", "Service"))
        item.setToolTip(_translate("KeyRing", "<html><head/><body><p>Login or Email that uses recent Service or Web Panel etc.</p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("KeyRing", "Username / EMail"))
        item.setToolTip(_translate("KeyRing", "<html><head/><body><p>Username or Email that uses Service or Web Panel etc.</p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("KeyRing", "Hashed Password"))
        item.setToolTip(_translate("KeyRing", "<html><head/><body><p>Hashed password with Specified earlier Salt Hash.</p></body></html>"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.Save.setText(_translate("KeyRing", "Save"))
        self.Edit.setText(_translate("KeyRing", "Edit"))
        self.Delete.setText(_translate("KeyRing", "Delete"))
        self.statusLabel.setText(_translate("KeyRing", "Server Status"))
        self.status.setText(_translate("KeyRing", "Status"))
        self.menuFile.setTitle(_translate("KeyRing", "File"))
        self.menuSettings.setTitle(_translate("KeyRing", "Settings"))
        self.menuAbout.setTitle(_translate("KeyRing", "Help"))
        self.actionSave.setText(_translate("KeyRing", "Save"))
        self.actionSave.setShortcut(_translate("KeyRing", "Ctrl+S"))
        self.actionSettings.setText(_translate("KeyRing", "Settings"))
        self.actionSettings.setShortcut(_translate("KeyRing", "Ctrl+E"))
        self.actionExit.setText(_translate("KeyRing", "Exit"))
        self.actionExit.setShortcut(_translate("KeyRing", "Ctrl+Q"))
        self.actionGeneral_Settings.setText(_translate("KeyRing", "General Settings"))
        self.actionAbout.setText(_translate("KeyRing", "About"))
