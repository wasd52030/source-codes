from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import random

app = QApplication(sys.argv)
root = QWidget()
root.setGeometry(500, 600, 300, 200)
root.setWindowTitle("DICE")
grid = QGridLayout(root)
root.setLayout(grid)

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
            lbls[index].setStyleSheet("color:red;")

def rangen():
    a=random.randint(1,6)
    rundice(a)

for i in range(3):
    for j in range(3):
        c = QLabel('●', root)
        c.setFixedSize(60, 50)
        c.setFont(QFont('Arial', 20))
        grid.addWidget(c, i, j)
        lbls.append(c)

b = QPushButton('run dice', root)
b.clicked.connect(rangen)
b.setFont(QFont('Arial', 20))
grid.addWidget(b, 4, 0, 3, 0)
b.setFixedSize(200, 80)


rundice(0)
root.show()
sys.exit(app.exec_())
