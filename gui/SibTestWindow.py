import os, config

import sys
from PyQt6 import uic, QtWidgets, QtCore
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon

os.chdir(config.project_path)  # переходим в корневую директорию проекта

Form, _ = uic.loadUiType(".\\gui\\WelcomeWindow.ui")


class Ui(QtWidgets.QDialog, Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon("logo.png"))
        self.setWindowTitle('SibTest')
        #self.setStyleSheet("background-color: grey;")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ui()
    window.show()
    app.exec()