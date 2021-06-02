import os
from threading import Timer
from tkinter import *
import random
import collections

root = Tk()
root.resizable(0, 0)

gameframe = Frame(root, bd=2, relief='groove')
gameframe.pack(side='bottom', pady=15)

payframe = Frame(root, bd=2, relief='groove')
payframe.pack(side='top')

ImageLst = []
ImageFileNames = []
Imagewithindex = []
ItemWithIndex = {}
lbls = []
BetForItem = []
BetPercentDict = {8-i: (i+1)**2 for i in range(8)}
BetUpBtns = []
BetDownBtns = []
WinBonusTemp = {}
WinBonus = []
n = 0
speedCtl, lvlCtl = 0, 0
speed = 0
ans = 0
money = 100
lblmoney = None
stopflag = False
lbla = None
itemcnt = {}


def data_init():
    global ans, speedCtl, lvlCtl, speed, stopflag, Imagewithindex, itemcnt, WinBonusTemp, WinBonus
    stopflag = False
    speed = 0.01
    ans = random.randint(0, 23)
    speedCtl, lvlCtl = 0, 0
    itemcnt = collections.Counter(Imagewithindex)


def main_anime():
    global n, speed, speedCtl, ans, lvlCtl, stopflag, lbla, BetUpBtns, BetDownBtns, BetPercentDict, itemcnt, WinBonus, WinBonusTemp, money, lbla

    t1 = Timer(speed, main_anime)
    t1.start()
    speedCtl += 1
    for i in BetUpBtns:
        i['state'] = 'disable'
    for i in BetDownBtns:
        i['state'] = 'disable'

    if speedCtl % 100 == 0:
        speed *= 10
        lvlCtl += 1

    if lvlCtl == 2:
        if ans == n:
            stopflag = True
            t1.cancel()
            for i in BetUpBtns:
                i['state'] = 'normal'
            for i in BetDownBtns:
                i['state'] = 'normal'
            p = BetPercentDict[itemcnt[str(ItemWithIndex[n])]]
            c = 0
            for i in range(len(WinBonus)):
                if WinBonus[i][0] == str(ItemWithIndex[n]):
                    c = WinBonus[i][1]
            f = p*c
            money += f
            lblmoney['text'] = f'你還有{money}塊'
            for i in BetForItem:
                i['text'] = '0'
            WinBonus = [[k, v] for k, v in WinBonusTemp.items()]

    # label預設背景顏色->SystemButtonFace
    if stopflag == False:
        if 6 <= n < 16 and n % 2 == 0:
            n += 2
            lbls[n]['bg'] = '#ff0000'
            lbls[n-2]['bg'] = 'SystemButtonFace'
        elif n == 16:
            n = 23
            lbls[n]['bg'] = '#ff0000'
            lbls[16]['bg'] = 'SystemButtonFace'
        elif 17 < n <= 23:
            n -= 1
            lbls[n]['bg'] = '#ff0000'
            lbls[n+1]['bg'] = 'SystemButtonFace'
        elif 0 < n <= 17 and n > 8 and n % 2 == 1:
            n -= 2
            lbls[n]['bg'] = '#ff0000'
            lbls[n+2]['bg'] = 'SystemButtonFace'
        elif n == 7:
            n = 0
            lbls[n]['bg'] = '#ff0000'
            lbls[7]['bg'] = 'SystemButtonFace'
        else:
            n += 1
            lbls[n]['bg'] = '#ff0000'
            lbls[n-1]['bg'] = 'SystemButtonFace'
        lbla['image'] = ItemWithIndex[n]


def run():
    data_init()
    main_anime()


def gameframe_initial():
    global ItemWithIndex, ImageFileNames, lbla, Imagewithindex, WinBonusTemp, WinBonus
    # 取images資料夾下的所有圖片，匯集成tkinter.PhotoImage之list
    x = 0
    k = [i for i in range(8)]
    for fname in os.listdir('images/'):
        file_dicrectory = os.path.join('images/', fname)
        ImageFileNames.append(fname.split('.')[0])
        WinBonusTemp[fname.split('.')[0]] = 0
        ImageLst.append(PhotoImage(file=f'{file_dicrectory}', name=fname.split('.')[0]))

    WinBonus = [[k, v] for k, v in WinBonusTemp.items()]

    for i in range(7):
        for j in range(7):
            w = random.sample(k, 1)[0]
            k.remove(w)
            if k == []:
                k = [i for i in range(8)]
            if i == 0 or i == 6:
                a = Label(gameframe, image=ImageLst[w])
                a.grid(row=i, column=j)
                lbls.append(a)
                ItemWithIndex[x] = ImageLst[w]
                Imagewithindex.append(ImageFileNames[w])
                x += 1
            elif j == 0 or j == 6:
                a = Label(gameframe, image=ImageLst[w], font=('標楷體', 15))
                a.grid(row=i, column=j)
                lbls.append(a)
                ItemWithIndex[x] = ImageLst[w]
                Imagewithindex.append(ImageFileNames[w])
                x += 1

    Imagewithindex.sort()
    b = Button(gameframe, height=2, width=5, text='開始', font=('標楷體', 15), relief='groove', command=run)
    b.grid(row=3, column=3)
    lbla = Label(gameframe)
    lbla.grid(row=4, column=1, columnspan=5)


def BetNumCalc(x, f):
    global BetForItem, money, WinBonus
    money -= 1
    lblmoney['text'] = f'你還有{money}塊'
    k = int(BetForItem[x]['text'])
    if f == '+':
        k += 1
    elif f == '-':
        if k > 0:
            k -= 1
    WinBonus[x][1] = k
    BetForItem[x]['text'] = k


def payframe_initial():
    global ImageLst, money, lblmoney, BetForItem, BetPercentDict, itemcnt, ImageFileNames, BetUpBtns, BetDownBtns
    lblmoney = Label(payframe, text=f'你還有{money}塊', font=('標楷體', 15))
    lblmoney.grid(row=0, column=(len(ImageFileNames)//2)-1, columnspan=3)
    Label(payframe, text='倍率：', font=('標楷體', 15)).grid(row=2, column=0)
    Label(payframe, text='投注數量：', font=('標楷體', 15)).grid(row=3, column=0)
    d = [[k, v] for k, v in sorted(itemcnt.most_common())]

    for i in range(len(d)):
        a = Label(payframe, image=ImageLst[i]).grid(row=1, column=i+1)
        Label(payframe, text=BetPercentDict[d[i][1]], font=('標楷體', 15)).grid(row=2, column=i+1)
        q = Label(payframe, text=0, font=('標楷體', 15))
        q.grid(row=3, column=i+1)
        BetForItem.append(q)
        bup = Button(payframe, text='+', font=('', 15), command=lambda x=i, f='+': BetNumCalc(x, f), relief='groove')
        bup.grid(row=4, column=i+1)
        BetUpBtns.append(bup)
        bdn = Button(payframe, text='-', font=('', 15), command=lambda x=i, f='-': BetNumCalc(x, f), relief='groove')
        bdn.grid(row=5, column=i+1)
        BetDownBtns.append(bdn)


def main():
    global itemcnt
    gameframe_initial()
    data_init()
    payframe_initial()
    root.mainloop()


main()
