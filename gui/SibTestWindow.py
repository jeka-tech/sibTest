
import sys
from PyQt6 import uic, QtWidgets, QtCore
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon


Form, _ = uic.loadUiType("WelcomeWindow.ui")


class Ui(QtWidgets.QDialog, Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon("logo.png"))
        self.setWindowTitle('SibTest')
        #self.setStyleSheet("background-color: grey;")


app = QApplication(sys.argv)
window = Ui()
window.show()
app.exec()