import sys

from PyQt5.QtWidgets import *
from RegisteredParcel import RegisteredParcel


class RegisteredContents(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.RegisteredParcel = RegisteredParcel()

    def initUI(self):
        self.setWindowTitle("AllDelivery")
        self.setFixedSize(1000, 600)

        btn1 = QPushButton('서적', self)
        btn1.resize(150, 80)
        btn1.move(290, 160)
        btn1.clicked.connect(self.RegisteredParcel)

        btn2 = QPushButton('의류/패션', self)
        btn2.resize(150, 80)
        btn2.move(440, 160)
        btn2.clicked.connect(self.RegisteredParcel)

        btn3 = QPushButton('전자제품', self)
        btn3.resize(150, 80)
        btn3.move(590, 160)
        btn3.clicked.connect(self.RegisteredParcel)

        btn4 = QPushButton('음식류', self)
        btn4.resize(150, 80)
        btn4.move(290, 240)
        btn4.clicked.connect(self.RegisteredParcel)

        btn5 = QPushButton('아동/유아', self)
        btn5.resize(150, 80)
        btn5.move(440, 240)
        btn5.clicked.connect(self.RegisteredParcel)

        btn6 = QPushButton('사무/문구', self)
        btn6.resize(150, 80)
        btn6.move(590, 240)
        btn6.clicked.connect(self.RegisteredParcel)

        btn7 = QPushButton('음반/비디오', self)
        btn7.resize(150, 80)
        btn7.move(290, 320)
        btn7.clicked.connect(self.RegisteredParcel)

        btn8 = QPushButton('의료/건강식품', self)
        btn8.resize(150, 80)
        btn8.move(440, 320)
        btn8.clicked.connect(self.RegisteredParcel)

        btn9 = QPushButton('스포츠/레저', self)
        btn9.resize(150, 80)
        btn9.move(590, 320)
        btn9.clicked.connect(self.RegisteredParcel)

        btn10 = QPushButton('생활/자동차용품', self)
        btn10.resize(150, 80)
        btn10.move(290, 400)
        btn10.clicked.connect(self.RegisteredParcel)

        btn11 = QPushButton('미용/화장품', self)
        btn11.resize(150, 80)
        btn11.move(440, 400)
        btn11.clicked.connect(self.RegisteredParcel)


        btn12 = QPushButton('기타', self)
        btn12.resize(150, 80)
        btn12.move(590, 400)
        btn12.clicked.connect(self.RegisteredParcel)


        label1 = QLabel("소포 내용물 선택", self)
        label1.resize(400, 100)
        label1.move(405, 40)
        font1 = label1.font()
        font1.setPointSize(25)
        font1.setFamily("나눔바른고딕")
        font1.setBold(True)
        label1.setFont(font1)


    def RegisteredParcel(self):
        self.close()
        self.RegisteredParcel.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RegisteredContents()
    ex.show()
    sys.exit(app.exec_())