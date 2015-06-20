# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login-dialog.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 200)
        Dialog.setMinimumSize(QtCore.QSize(400, 200))
        Dialog.setMaximumSize(QtCore.QSize(400, 200))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 45, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(130, 40, 240, 40))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 95, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 90, 240, 40))
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.okBtn = QtWidgets.QPushButton(self.groupBox)
        self.okBtn.setGeometry(QtCore.QRect(210, 140, 80, 30))
        self.okBtn.setStyleSheet("background: lightblue;")
        self.okBtn.setObjectName("okBtn")
        self.cancelBtn = QtWidgets.QPushButton(self.groupBox)
        self.cancelBtn.setGeometry(QtCore.QRect(292, 140, 80, 30))
        self.cancelBtn.setObjectName("cancelBtn")
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Authentication"))
        self.groupBox.setTitle(_translate("Dialog", "Authentication"))
        self.label.setText(_translate("Dialog", "Username"))
        self.label_2.setText(_translate("Dialog", "Password"))
        self.okBtn.setText(_translate("Dialog", "OK"))
        self.cancelBtn.setText(_translate("Dialog", "Cancel"))

