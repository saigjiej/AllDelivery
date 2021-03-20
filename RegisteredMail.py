import sys
from PyQt5.QtWidgets import *
from Pay import Pay


class RegisteredMail(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.Pay = Pay()

    def setupUI(self):
        self.setWindowTitle("AllDelivery")
        self.setFixedSize(1000, 600)

        label = QLabel("등기 우편", self)
        label.move(435, 40)
        label.resize(500, 100)
        font1 = label.font()
        font1.setPointSize(30)
        font1.setFamily("나눔바른고딕")
        font1.setBold(True)
        label.setFont(font1)

        label2 = QLabel("보내는 사람", self)
        label2.move(150, 115)
        label2.resize(500, 100)
        font2 = label2.font()
        font2.setPointSize(15)
        font2.setFamily("나눔바른고딕")
        font2.setBold(True)
        label2.setFont(font2)

        label3 = QLabel("성명", self)
        label3.move(150, 160)
        label3.resize(500, 100)
        font3 = label3.font()
        font3.setPointSize(13)
        font3.setFamily("나눔바른고딕")
        label3.setFont(font3)
        textEdit1 = QTextEdit(self)
        textEdit1.resize(150, 25)
        textEdit1.move(200, 195)

        label4 = QLabel("주소", self)
        label4.move(150, 205)
        label4.resize(500, 100)
        font4 = label4.font()
        font4.setPointSize(13)
        font4.setFamily("나눔바른고딕")
        label4.setFont(font4)
        textEdit2 = QTextEdit(self)
        textEdit2.resize(350, 25)
        textEdit2.move(200, 240)

        label5 = QLabel("전화번호", self)
        label5.move(150, 250)
        label5.resize(500, 100)
        font5 = label5.font()
        font5.setPointSize(13)
        font5.setFamily("나눔바른고딕")
        label5.setFont(font5)
        textEdit3 = QTextEdit(self)
        textEdit3.resize(350, 25)
        textEdit3.move(230, 285)

        label6 = QLabel("받는 분", self)
        label6.move(150, 310)
        label6.resize(500, 100)
        font6 = label6.font()
        font6.setPointSize(15)
        font6.setFamily("나눔바른고딕")
        font6.setBold(True)
        label6.setFont(font6)

        label7 = QLabel("성명", self)
        label7.move(150, 355)
        label7.resize(500, 100)
        font7 = label7.font()
        font7.setPointSize(13)
        font7.setFamily("나눔바른고딕")
        label7.setFont(font7)
        textEdit4 = QTextEdit(self)
        textEdit4.resize(150, 25)
        textEdit4.move(200, 393)

        label8 = QLabel("주소", self)
        label8.move(150, 400)
        label8.resize(500, 100)
        font8 = label8.font()
        font8.setPointSize(13)
        font8.setFamily("나눔바른고딕")
        label8.setFont(font8)
        textEdit5 = QTextEdit(self)
        textEdit5.resize(350, 25)
        textEdit5.move(200, 435)

        label9 = QLabel("전화번호", self)
        label9.move(150, 445)
        label9.resize(500, 100)
        font9 = label9.font()
        font9.setPointSize(13)
        font9.setFamily("나눔바른고딕")
        label9.setFont(font9)
        textEdit6 = QTextEdit(self)
        textEdit6.resize(350, 25)
        textEdit6.move(230, 480)

        label10 = QLabel("보낼 메시지", self)
        label10.move(660, 125)
        label10.resize(500, 100)
        font10 = label10.font()
        font10.setPointSize(15)
        font10.setBold(True)
        font10.setFamily("나눔바른고딕")
        label10.setFont(font10)
        textEdit7 = QTextEdit(self)
        textEdit7.resize(240, 230)
        textEdit7.move(660, 200)

        btn1 = QPushButton("확인", self)
        btn1.move(770, 445)
        btn1.resize(130, 60)

        btn1.clicked.connect(self.Pay)

    def Pay(self):
        self.close()
        self.Pay.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = RegisteredMail()
    mywindow.show()
    app.exec_()