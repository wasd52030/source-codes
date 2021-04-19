from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import re
import sys
import random
import time

app = QApplication(sys.argv)
root = QWidget()
root.setFixedSize(0,0)
grid = QGridLayout(root)
root.setLayout(grid)

n = x = 0
a = []
ans = []
btns = []
t1 = t2 = time.time()

def numlist_init():
    k = [k for k in range(10)]
    g = []
    random.shuffle(k)
    for i in range(1, 19):
        w = random.sample(k, 1)
        g.append(w[0])
        g.append(w[0])
    random.shuffle(g)
    return g

def gamedata_init():
    ans.clear()

def run(bid):
    global n, x, t1, t2, a, ans, btns

    if n == 0:
        t1 = time.time()
    ans.append(btns[bid])
    btns[bid].setEnabled(False)

    if len(ans) == 2:
        if ans[0].text() == ans[1].text():
            btns[bid].setEnabled(False)
            n+= 1
        else:
            for k in ans: k.setEnabled(True)
        gamedata_init()

    if n == len(btns)/2:
        t2 = time.time()
        reply = QMessageBox.warning(root,'',f'共用{t2-t1}秒\n要重新開始嗎?\n如選擇NO將直接結束',QMessageBox.Yes | QMessageBox.No)
        n = x = 0
        btns.clear()
        a.clear()
        if reply == QMessageBox.Yes:
            game_window_init()
        else:
            sys.exit(0)

def game_window_init():
    global a, x
    a = numlist_init()
    for i in range(0, 6):
        for j in range(0, 6):
            b = QPushButton(str(a[x]), root)
            b.clicked.connect(lambda state,id=x: run(id))
            b.setFont(QFont('Arial', 20))
            grid.addWidget(b, i, j)
            btns.append(b)
            x += 1

def main():
    game_window_init()
    root.show()
    sys.exit(app.exec_())

main()