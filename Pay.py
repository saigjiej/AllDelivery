import sys
from PyQt5.QtWidgets import *
from PayCompletion import PayCompletion


class Pay(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.PayCompletion = PayCompletion()

    def setupUI(self):
        self.setWindowTitle("AllDelivery")
        self.setFixedSize(1000, 600)

        btn1 = QPushButton('신용카드\n(체크카드)', self)
        btn1.resize(250, 120)
        btn1.move(245, 200)
        btn1.clicked.connect(self.PayCompletion)

        btn2 = QPushButton('휴대폰', self)
        btn2.resize(250, 120)
        btn2.move(525, 200)
        btn2.clicked.connect(self.PayCompletion)

        btn3 = QPushButton('현금', self)
        btn3.resize(250, 120)
        btn3.move(525, 350)
        btn3.clicked.connect(self.PayCompletion)

        btn4 = QPushButton('T-money', self)
        btn4.resize(250, 120)
        btn4.move(245, 350)
        btn4.clicked.connect(self.PayCompletion)


        label1 = QLabel("결제방법을 선택해 주세요", self)
        label1.resize(400, 100)
        label1.move(340, 60)
        font1 = label1.font()
        font1.setPointSize(25)
        font1.setFamily("나눔바른고딕")
        font1.setBold(True)
        label1.setFont(font1)

    def PayCompletion(self):
        self.close()
        self.PayCompletion.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = Pay()
    mywindow.show()
    app.exec_()