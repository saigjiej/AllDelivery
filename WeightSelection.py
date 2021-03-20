import sys
from PyQt5.QtWidgets import *
from Pay import Pay


class WeightSelection(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.Pay = Pay()

    def initUI(self):
        self.setWindowTitle("AllDelivery")
        self.setFixedSize(1000, 600)

        btn1 = QPushButton('무게(3kg)\n크기(80cm) 이하\n4,000원', self)
        btn1.resize(200, 90)
        btn1.move(220, 160)
        btn1.clicked.connect(self.Pay)

        btn2 = QPushButton('무게(5kg)\n크기(100cm) 이하\n4,500원', self)
        btn2.resize(200, 90)
        btn2.move(420, 160)
        btn2.clicked.connect(self.Pay)

        btn3 = QPushButton('무게(7kg)\n크기(100cm) 이하\n5,000원', self)
        btn3.resize(200, 90)
        btn3.move(620, 160)
        btn3.clicked.connect(self.Pay)

        btn4 = QPushButton('무게(10kg)\n크기(120cm) 이하\n6,000원', self)
        btn4.resize(200, 90)
        btn4.move(220, 250)
        btn4.clicked.connect(self.Pay)

        btn5 = QPushButton('무게(15kg)\n크기(120cm) 이하\n7,000원', self)
        btn5.resize(200, 90)
        btn5.move(420, 250)
        btn5.clicked.connect(self.Pay)

        btn6 = QPushButton('무게(20kg)\n크기(120cm) 이하\n8,000원', self)
        btn6.resize(200, 90)
        btn6.move(620, 250)
        btn6.clicked.connect(self.Pay)

        btn7 = QPushButton('무게(25kg)\n크기(120cm) 이하\n9,000원', self)
        btn7.resize(200, 90)
        btn7.move(220, 340)
        btn7.clicked.connect(self.Pay)

        btn8 = QPushButton('무게(30kg)\n크기(160cm) 이하\n11,000원', self)
        btn8.resize(200, 90)
        btn8.move(420, 340)
        btn8.clicked.connect(self.Pay)

        label1 = QLabel("우체국 소포 요금", self)
        label1.resize(400, 100)
        label1.move(405, 50)
        font1 = label1.font()
        font1.setPointSize(25)
        font1.setFamily("나눔바른고딕")
        font1.setBold(True)
        label1.setFont(font1)


    def Pay(self):
        self.close()
        self.Pay.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WeightSelection()
    ex.show()
    sys.exit(app.exec_())