import os, config
from PyQt6 import uic, QtWidgets

os.chdir(config.project_path)  # переходим в корневую директорию проекта

Form, _ = uic.loadUiType('.\\gui\\TestWindow.ui')

otvet = "0"


class Ui_2(QtWidgets.QDialog, Form):
    def __init__(self):
        super(Ui_2, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('SibTest')
        self.buttonGroup.buttonClicked.connect(self.choise)
        self.pushButton.clicked.connect(self.onMyButtonClick_2)


    def onMyButtonClick_2(self):
        global otvet
        if otvet == "0":
            self.label_2.setText("Ответ не выбран")
        elif otvet == "rb1":
            self.label_2.setText("Верно")
            self.pushButton_2.setStyleSheet('QPushButton {background-color: green}')
        elif otvet == "rb2":
            self.label_2.setText("Не верно")
            self.pushButton_2.setStyleSheet('QPushButton {background-color: red}')
        elif otvet == "rb3":
            self.label_2.setText("Не верно")
            self.pushButton_2.setStyleSheet('QPushButton {background-color: red}')

    def choise(self, button):
        global otvet
        otvet = button.objectName()


