import sys
from PyQt5.QtWidgets import QApplication
from application.auth import LoginDialog
from application.core import KeyRing

if __name__ == "__main__":
  a = QApplication(sys.argv)

  loginDialog = LoginDialog()

  isAuth = False
  result = -1
  while not isAuth:
    result = loginDialog.exec_()
    if result == LoginDialog.Success or result == LoginDialog.Rejected:
      isAuth = True
    else:
      isAuth = False

  if result == LoginDialog.Success:
    w = KeyRing()
    w.show()
    a.exec_()

  sys.exit(-1)