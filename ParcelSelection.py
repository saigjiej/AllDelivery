import sys
from PyQt5.QtWidgets import *
from GeneralContents import GeneralContents
from RegisteredContents import RegisteredContents


class ParcelSelection(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.GeneralContents = GeneralContents()
        self.RegisteredContents = RegisteredContents()

    def setupUI(self):
        self.setWindowTitle("AllDelivery")
        self.setFixedSize(1000, 600)

        label = QLabel("소포", self)
        label.move(450, 100)
        label.resize(130, 60)
        font1 = label.font()
        font1.setPointSize(50)
        font1.setFamily("나눔바른고딕")
        font1.setBold(True)
        label.setFont(font1)

        label2 = QLabel("1kg 이상 30kg 이하의 소포 우편서비스", self)
        label2.move(350, 120)
        label2.resize(400, 130)
        font2 = label2.font()
        font2.setFamily("나눔바른고딕")
        font2.setPointSize(15)
        label2.setFont(font2)

        btn1 = QPushButton("일반 소포", self)
        btn1.move(150, 300)
        btn1.resize(300,150)
        btn1.clicked.connect(self.GeneralContents)

        btn2 = QPushButton("등기 소포", self)
        btn2.move(570, 300)
        btn2.resize(300,150)
        btn2.clicked.connect(self.RegisteredContents)

    def GeneralContents(self):
        self.close()
        self.GeneralContents.show()

    def RegisteredContents(self):
        self.close()
        self.RegisteredContents.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = ParcelSelection()
    mywindow.show()
    app.exec_()