import sys
import random
import time
from functools import partial
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

app = QApplication(sys.argv)
root = QWidget()
root.setFixedSize(0, 0)
grid = QGridLayout(root)
root.setLayout(grid)

n, x = 0, 0
a, ans, btns = [], [], []
t1, t2 = time.time(), time.time()
timer = QTimer(root)

def numlist_init():
    g = []
    for i in range(1, 19):
        w = random.randint(1,10)
        g.append(w)
        g.append(w)
    random.shuffle(g)
    return g

def clearText():
    global ans
    if len(ans) != 0:
        for i in ans:
            i.setText('')
            i.setEnabled(True)
    ans.clear()
    timer.stop()

timer.timeout.connect(clearText)

def run(bid):
    global n, x, t1, t2, a, ans, btns, timer

    if n == 0: t1 = time.time()
    btns[bid].setEnabled(False) 
    btns[bid].setText(str(a[bid]))
    ans.append(btns[bid])
    if len(ans) == 2:
        if ans[0].text() == ans[1].text():
            n += 1
            ans.clear()
        else:
            timer.start(150)
        

    if n == len(btns)/2:
        t2 = time.time()
        reply = QMessageBox.warning( root, '', f'共用{t2-t1}秒\n要重新開始嗎?\n如選擇NO將直接結束', QMessageBox.Yes | QMessageBox.No)
        n, x = 0, 0
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
            b = QPushButton(root)
            b.clicked.connect(partial(run,x))
            b.setFont(QFont('Arial', 20))
            b.setStyleSheet('border: 3px solid;border-radius:5px;width:80px;height:80px;')
            grid.addWidget(b, i, j)
            btns.append(b)
            x += 1

def main():
    game_window_init()
    root.show()
    sys.exit(app.exec_())

main()
