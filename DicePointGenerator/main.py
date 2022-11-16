from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys
import random

app = QApplication(sys.argv)
root = QWidget()
root.setWindowTitle('dice') #設定視窗標題
root.resize(270, 365)
root.setFixedSize(270, 365)

dice = QWidget(root)
dice.setGeometry(QRect(10, 20, 250, 250))
dice.setObjectName("dice")

dicegrid = QGridLayout(root)
dice.setLayout(dicegrid)

# 載入qss樣式檔(qt系特有的樣式檔，講人話就是qt專用的css)
with open('./style.qss') as mainqss:
    qss = mainqss.read()
    app.setStyleSheet(qss)

lbls = []
points = {
    0: [0 for i in range(9)],
    1: [1 if i == 4 else 0 for i in range(9)],
    2: [1 if i in [0, 8] else 0 for i in range(9)],
    3: [1 if i in [0, 4, 8] else 0 for i in range(9)],
    4: [1 if i in [0, 2, 6, 8] else 0 for i in range(9)],
    5: [1 if i in [0, 2, 4, 6, 8] else 0 for i in range(9)],
    6: [1 if i in [0, 2, 3, 5, 6, 8] else 0 for i in range(9)],
}


# 當同時需要list的元素和索引時，可用enumerate(list)做迭代
def rundice(x):
    for index, item in enumerate(points[x]):
        if item == 0:
            lbls[index].setStyleSheet("color:transparent;")
        elif item == 1:
            if x == 1:
                lbls[index].setStyleSheet("color:red;")
            else:
                lbls[index].setStyleSheet("color:black;")


def rangen():
    global timer1Cnt, timer1speed
    a = random.randint(1, 6)
    rundice(a)
    if timer1Cnt == 50:
        timer1.stop()
    else:
        if timer1Cnt % 5 == 0:
            timer1speed *= 10
        timer1Cnt += 1


def GetPoint():
    global timer1Cnt, timer1speed
    timer1Cnt, timer1speed = 0, 10
    timer1.start(timer1speed)


for i in range(3):
    for j in range(3):
        c = QLabel('●', root)
        c.setFixedSize(60, 50)
        c.setFont(QFont('Arial', 30))
        c.setAlignment(Qt.AlignCenter)
        dicegrid.addWidget(c, i, j)
        lbls.append(c)

b = QPushButton('run dice', root)
b.clicked.connect(GetPoint)
b.setFont(QFont('Arial', 20))
b.setGeometry(QRect(10, 280, 250, 71))
b.setObjectName("b")

timer1 = QTimer(root)
timer1.timeout.connect(rangen)
timer1Cnt = 0
timer1speed = 10

rundice(random.randint(1, 6))
root.show()
sys.exit(app.exec_())
