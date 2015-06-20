from PyQt5.QtWidgets import QMainWindow
from ui.ui_keyring import Ui_KeyRing
from application.dialogs.about import AboutDialog

class KeyRing(QMainWindow, Ui_KeyRing):
  def __init__(self):
    QMainWindow.__init__(self)
    self.setupUi(self)
    self.actionAbout.triggered.connect(self.About)
    self.actionExit.triggered.connect(self.close)
    # Save actions
    self.actionSave.triggered.connect(self.saveData)
    self.Save.clicked.connect(self.saveData)

  def About(self):
    self.setWindowOpacity(0.2)
    self.setDisabled(True)
    dialog = AboutDialog(self)
    dialog.show()

  def saveData(self):
    print('Save')
