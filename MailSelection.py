import sys
from PyQt5.QtWidgets import *
from GeneralMail import GeneralMail
from RegisteredMail import RegisteredMail
from InternationalMail import InternationalMail


class MailSelection(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.GeneralMail = GeneralMail()
        self.RegisteredMail = RegisteredMail()
        self.InternationalMail = InternationalMail()

    def setupUI(self):
        self.setWindowTitle("AllDelivery")
        self.setFixedSize(1000, 600)

        label = QLabel("우편", self)
        label.move(450, 100)
        label.resize(130, 100)
        font1 = label.font()
        font1.setPointSize(50)
        font1.setFamily("나눔바른고딕")
        font1.setBold(True)
        label.setFont(font1)

        btn1 = QPushButton("일반 우편", self)
        btn1.move(130, 300)
        btn1.resize(250, 150)
        btn1.clicked.connect(self.GeneralMail)

        btn2 = QPushButton("등기 우편", self)
        btn2.move(390, 300)
        btn2.resize(250, 150)
        btn2.clicked.connect(self.RegisteredMail)

        btn3 = QPushButton("국제 우편", self)
        btn3.move(650, 300)
        btn3.resize(250, 150)
        btn3.clicked.connect(self.InternationalMail)

    def GeneralMail(self):
        self.close()
        self.GeneralMail.show()

    def RegisteredMail(self):
        self.close()
        self.RegisteredMail.show()

    def InternationalMail(self):
        self.close()
        self.InternationalMail.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MailSelection()
    mywindow.show()
    app.exec_()
