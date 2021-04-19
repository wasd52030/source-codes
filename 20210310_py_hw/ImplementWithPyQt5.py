import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import re

app = QApplication(sys.argv)
root = QWidget()
root.setFixedSize(0,0)
grid = QGridLayout(root)
root.setLayout(grid)

s = '0'
btn_txt = ['7', '8', '9', '*', '4', '5', '6', '-', '1', '2', '3', '+']

def run(g):
    global s
    if s == '0':
        s = g
    else:
        s += g
    x.setText(s)

def clear():
    global s
    s = '0'
    x.setText(s)

def calc():
    global s
    s = str(eval(s))
    x.setText(s)

x = QLabel(s, root)
x.setAlignment(Qt.AlignRight)
x.setFont(QFont('Arial', 20))
grid.addWidget(x, 0, 0, 1, 4)

C = QPushButton('C', root)
C.clicked.connect(clear)
C.setFont(QFont('Arial', 20))
grid.addWidget(C, 1, 0, 1, 3)

dev = QPushButton('/', root)
dev.clicked.connect(lambda state, g='/': run(g))
dev.setFont(QFont('Arial', 20))
grid.addWidget(dev, 1, 3)

zero = QPushButton('0', root)
zero.clicked.connect(lambda state, g='0': run(g))
zero.setFont(QFont('Arial', 20))
grid.addWidget(zero, 5, 0, 1, 2)

dot = QPushButton('.', root)
dot.clicked.connect(lambda state, g='.': run(g))
dot.setFont(QFont('Arial', 20))
grid.addWidget(dot, 5, 2)

equal = QPushButton('=', root)
equal.clicked.connect(calc)
equal.setFont(QFont('Arial', 20))
grid.addWidget(equal, 5, 3)

# grid.addWidget (self, QWidget, row, column, rowSpan, columnSpan, Qt.Alignment alignment = 0)
# 第三個和第四個引數是行和列跨越，預設情況下等於 1。如果跨度為-1，則單元格控制元件將延伸到右邊或底邊。
#about how to use button.clicked.connect(lambda ....), see https://stackoverflow.com/questions/35819538/using-lambda-expression-to-connect-slots-in-pyqt
r = 0
for i in range(2, 5):
    for j in range(0, 4):
        b = QPushButton(btn_txt[r], root)
        b.clicked.connect(lambda state, g=btn_txt[r]: run(g))
        b.setFont(QFont('Arial', 20))
        grid.addWidget(b, i, j)
        r += 1

root.show()
sys.exit(app.exec_())