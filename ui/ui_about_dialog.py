# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about-dialog.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 300)
        Dialog.setMinimumSize(QtCore.QSize(500, 300))
        Dialog.setMaximumSize(QtCore.QSize(500, 300))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.aboutFrame = QtWidgets.QFrame(Dialog)
        self.aboutFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.aboutFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.aboutFrame.setObjectName("aboutFrame")
        self.gridLayout.addWidget(self.aboutFrame, 0, 0, 1, 1)
        self.okButton = QtWidgets.QPushButton(Dialog)
        self.okButton.setObjectName("okButton")
        self.gridLayout.addWidget(self.okButton, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "About 'Leo Key Chain'"))
        self.okButton.setText(_translate("Dialog", "OK"))

