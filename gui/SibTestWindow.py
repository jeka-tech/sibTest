import os, config

import sys

from PyQt6 import uic, QtWidgets, QtCore
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon
from TestWindow import Ui_2

os.chdir(config.project_path)  # переходим в корневую директорию проекта

Form, _ = uic.loadUiType('.\\gui\\WelcomeWindow.ui')


class Ui(QtWidgets.QDialog, Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('.\\gui\\logo.png'))
        self.setWindowTitle('SibTest')
        self.lineEdit.setPlaceholderText('user name')
        self.pushButton.clicked.connect(self.Open_TestWindow)
        self.pushButton.clicked.connect(self.UserName)

    def UserName(self):
        print(self.lineEdit.text())

    def Open_TestWindow(self):
        self.open = Ui_2()
        self.open.show()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ui()
    window.show()
    app.exec()


