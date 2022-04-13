from threading import Timer
from tkinter import *
import random

root = Tk()
root.resizable(0, 0)
gameframe = Frame(root, bd=2, relief='groove')
gameframe.pack(side='top')

funcframe = Frame(root)
funcframe.pack(side='bottom', pady=15)

ans = []
ansmap = [[0 for i in range(10)] for i in range(10)]
TimeText = StringVar()
gridbtns = []
btnsarr = []
cnt = 0
stopflag = False


def setans():
    global ans, ansmap
    s = 0
    ans.clear()
    ansmap = [[0 for i in range(10)] for i in range(10)]
    while len(ans) < 10:
        r = [random.randint(0, 9), random.randint(0, 9)]
        if r not in ans:
            ans.append(r)
            # 把定做地雷的元素設-1
            ansmap[r[0]][r[1]] = -1
            s += 1

    for i in ansmap:
        for j in i:
            print(f'{j:2d}',end='')
        print()
    print()


def timecnt():
    global cnt, TimeText, stopflag, btnsarr
    t1 = Timer(1, timecnt)
    t1.start()
    if stopflag == True:
        t1.cancel()
        for i in btnsarr:
            i['state'] = 'disabled'
    else:
        TimeText.set(cnt)
        cnt += 1


def reset():
    global cnt, stopflag, gridbtns
    cnt = 0
    stopflag = False

    for i in range(len(gridbtns)):
        for j in range(len(gridbtns[0])):
            gridbtns[i][j]['text'] = ''
            gridbtns[i][j]['state'] = 'normal'

    setans()
    timecnt()


def judgment(x, y):
    global ansmap, stopflag, gridbtns, btnsarr
    gridbtns[x][y]['state'] = 'disabled'
    r = 0
    k = []

    if ansmap[x][y] == 0:
        if x in [0, 9] or y in [0, 9]:
            # 劃定以按下去的按鈕做左上第一顆，面積為9的領域
            for i in range(x, x+3):
                for j in range(y, y+3):
                    if x > 8:
                        u = i-2
                    elif x > 7:
                        u = i-1
                    else:
                        u = i

                    if y > 8:
                        v = j-2
                    elif y > 7:
                        v = j-1
                    else:
                        v = j
                    k.append([u, v])
        else:
            # 劃定以按下去的按鈕做中心點，面積為9的領域
            for i in range(x-2, x+1):
                for j in range(y-2, y+1):
                    k.append([i+1, j+1])

        # 處理對劃定領域中的地雷狀態
        for i in k:
            if ansmap[i[0]][i[1]] == 0:
                gridbtns[i[0]][i[1]]['text'] = '0'
                gridbtns[i[0]][i[1]]['state'] = 'disabled'
            elif ansmap[i[0]][i[1]] == -1:
                r += 1

        gridbtns[x][y]['text'] = r
        n = [i for i in btnsarr if i['state'] == 'normal']

        if len(n) == len(ans):
            stopflag = True
    elif ansmap[x][y] == -1:
        stopflag = True
        for j in ans:
            gridbtns[j[0]][j[1]]['text'] = 'X'
        for u in range(len(gridbtns)):
            for v in range(len(gridbtns[0])):
                gridbtns[u][v]['state'] = 'disabled'


def game_init():
    global gridbtns, btnsarr
    for i in range(10):
        r = []
        for j in range(10):
            b = Button(gameframe, height=2, width=4, command=lambda x=i, y=j: judgment(x, y))
            b.grid(row=i, column=j)
            btnsarr.append(b)
            r.append(b)
        gridbtns.append(r)
    Label(funcframe, textvariable=TimeText, font=('標楷體', 15)).pack(side='left', padx=90)
    Button(funcframe, text='重置', font=('標楷體', 15), command=reset, relief='groove').pack(side='right')


def main():
    setans()
    game_init()
    timecnt()
    root.mainloop()


main()
