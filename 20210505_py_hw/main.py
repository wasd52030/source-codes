import os
from threading import Timer
from tkinter import *
import random

ImageLst = []
ImageFileNames = []
ItemWithIndex = {}
lbls = []
n = 0
speedCtl, lvlCtl = 0, 0
speed = 0
ans = 0
stopflag = False
lbla = None
root = Tk()


def data_init():
    global ans, speedCtl, lvlCtl, speed, stopflag, ItemWithIndex
    stopflag = False
    speed = 0.01
    ans = random.randint(0, 23)
    speedCtl, lvlCtl = 0, 0


def main_anime():
    global n, speed, speedCtl, ans, lvlCtl, stopflag, lbla

    t1 = Timer(speed, main_anime)
    t1.start()
    speedCtl += 1

    if speedCtl % 50 == 0:
        speed *= 10
        lvlCtl += 1

    if lvlCtl == 2:
        if ans == n:
            stopflag = True
            t1.cancel()

    #label預設背景顏色->SystemButtonFace
    if stopflag == False:
        if 6 <= n < 16 and n % 2 == 0:
            n += 2
            lbla['text'] = ItemWithIndex[n]
            lbls[n]['bg'] = '#ff0000'
            lbls[n-2]['bg'] = 'SystemButtonFace'
        elif n == 16:
            n = 23
            lbla['text'] = ItemWithIndex[n]
            lbls[n]['bg'] = '#ff0000'
            lbls[16]['bg'] = 'SystemButtonFace'
        elif 17 < n <= 23:
            n -= 1
            lbla['text'] = ItemWithIndex[n]
            lbls[n]['bg'] = '#ff0000'
            lbls[n+1]['bg'] = 'SystemButtonFace'
        elif 0 < n <= 17 and n > 8 and n % 2 == 1:
            n -= 2
            lbla['text'] = ItemWithIndex[n]
            lbls[n]['bg'] = '#ff0000'
            lbls[n+2]['bg'] = 'SystemButtonFace'
        elif n == 7:
            n = 0
            lbla['text'] = ItemWithIndex[n]
            lbls[n]['bg'] = '#ff0000'
            lbls[7]['bg'] = 'SystemButtonFace'
        else:
            n += 1
            lbla['text'] = ItemWithIndex[n]
            lbls[n]['bg'] = '#ff0000'
            lbls[n-1]['bg'] = 'SystemButtonFace'


def run():
    data_init()
    main_anime()


def initial():
    global ItemWithIndex, ImageFileNames, lbla
    # 取images資料夾下的所有圖片，匯集成tkinter.PhotoImage之list
    x = 0
    for fname in os.listdir('images/'):
        file_dicrectory = os.path.join('images/', fname)
        ImageFileNames.append(fname.split('.')[0])
        ImageLst.append(PhotoImage(file=f'{file_dicrectory}'))

    for i in range(7):
        for j in range(7):
            w = random.randint(0, 7)
            if i == 0 or i == 6:
                a = Label(root, image=ImageLst[w])
                a.grid(row=i, column=j)
                lbls.append(a)
                ItemWithIndex[x] = ImageFileNames[w]
                x += 1
            elif j == 0 or j == 6:
                a = Label(root, image=ImageLst[w])
                a.grid(row=i, column=j)
                lbls.append(a)
                ItemWithIndex[x] = ImageFileNames[w]
                x += 1

    b = Button(root, height=2, width=5,relief='groove', text='開始', command=run)
    b.grid(row=3, column=3)
    lbla = Label(root, text='')
    lbla.grid(row=4, column=1, columnspan=5)


def main():
    initial()
    data_init()
    root.mainloop()


main()