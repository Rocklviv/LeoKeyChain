__author__ = 'dchekirda'
from PyQt5.QtWidgets import QDialog
from ui.ui_about_dialog import Ui_Dialog

class AboutDialog(QDialog, Ui_Dialog):

  def __init__(self, parent = None):
    QDialog.__init__(self, parent)
    self.setupUi(self)
    self.okButton.clicked.connect(self.closeUp)
    self.parent = parent

  def closeUp(self):
    self.close()
    self.parent.setWindowOpacity(1.0)
    self.parent.setDisabled(False)