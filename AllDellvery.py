import sys

from PyQt5.QtWidgets import *
from PySide2.QtWidgets import QMainWindow

from MailSelection import MailSelection
from ParcelSelection import ParcelSelection


class AllDellvery(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.MailSelection = MailSelection()
        self.ParcelSelection = ParcelSelection()

    def setupUI(self):
        self.setWindowTitle("AllDelivery")
        self.setFixedSize(1000, 600)

        label = QLabel("모두의 배송", self)
        label.move(350, 80)
        label.resize(402, 100)
        font1 = label.font()
        font1.setPointSize(50)
        font1.setFamily("나눔바른고딕")
        font1.setBold(True)
        label.setFont(font1)

        label2 = QLabel("모두의 배송에 오신 것을 환영합니다:)", self)
        label2.move(360, 120)
        label2.resize(400, 130)
        font2 = label2.font()
        font2.setFamily("나눔바른고딕")
        font2.setPointSize(15)
        label2.setFont(font2)

        btn1 = QPushButton("우편", self)
        btn1.move(155, 300)
        btn1.resize(300, 150)
        btn1.clicked.connect(self.MailSelection)

        btn2 = QPushButton("소포", self)
        btn2.move(570, 300)
        btn2.resize(300, 150)
        btn2.clicked.connect(self.ParcelSelection)

    def MailSelection(self):
        self.close()
        self.MailSelection.show()

    def ParcelSelection(self):
        self.close()
        self.ParcelSelection.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = AllDellvery()
    mywindow.show()
    app.exec_()