from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import random
import time

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
    k = [k for k in range(10)]
    g = []
    random.shuffle(k)
    for i in range(1, 19):
        w = random.sample(k, 1)
        g.append(w[0])
        g.append(w[0])
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
            b.clicked.connect(lambda state, id=x: run(id))
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
