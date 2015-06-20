__author__ = 'dchekirda'
import sys
from PyQt5.QtWidgets import QDialog
from ui.ui_login_dialog import Ui_Dialog

class LoginDialog(QDialog, Ui_Dialog):
  Success,Failed,Rejected = range(0,3)

  def __init__(self):
    QDialog.__init__(self)
    self.setupUi(self)
    self.okBtn.clicked.connect(self.onAccept)
    self.cancelBtn.clicked.connect(self.onReject)

  def onAccept(self):
    self.setResult(self.Success)
    self.close()

  def onReject(self):
    sys.exit(-1)