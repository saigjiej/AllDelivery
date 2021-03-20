import importlib
import sys
from PyQt5.QtWidgets import *


class PayCompletion(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()


    def setupUI(self):
        self.setWindowTitle("AllDelivery")
        self.setFixedSize(1000, 600)

        btn1 = QPushButton('완료', self)
        btn1.resize(250, 120)
        btn1.move(380, 300)
        btn1.clicked.connect(self.AllDellvery)

        label1 = QLabel("결제가 완료되었습니다!", self)
        label1.resize(400, 100)
        label1.move(350, 100)
        font1 = label1.font()
        font1.setPointSize(25)
        font1.setFamily("나눔바른고딕")
        font1.setBold(True)
        label1.setFont(font1)

        label2 = QLabel("모두의 배송을 사용해주셔서 감사하며, 완료버튼 클릭 시 창이 꺼집니다.", self)
        label2.resize(600, 100)
        label2.move(275, 150)
        font2 = label2.font()
        font2.setPointSize(12)
        font2.setFamily("나눔바른고딕")
        font2.setBold(True)
        label2.setFont(font2)

    def AllDellvery(self):
        self.close()
        self.AllDellvery.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = PayCompletion()
    mywindow.show()
    app.exec_()
