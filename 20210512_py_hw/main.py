import random
from tkinter import *
import tkinter.font

with open('eng.txt', 'r', encoding='utf-8') as f1:
    data = [i.split() for i in f1]

root = Tk()
x = random.randint(0, len(data)-1)
score = 0
ans = StringVar()


def eng(engTxt):
    global data
    k = 0.8*len(data[x][0])
    for i in range(int(k)):
        p = random.randint(0, len(engTxt)-1)
        engTxt = f'{engTxt[:p]}*{engTxt[p+1:]}'
    return engTxt


def run():
    global x, ans, score
    if ans.get() == data[x][0]:
        score += 1
        sc['text'] = f'分數: {score}'
    x = random.randint(0, len(data)-1)
    e2['text'] = eng(data[x][0])
    c2['text'] = data[x][1]
    ans.set('')


e1 = Label(root, text='英文：', font=tkinter.font.Font(family="Arial", size=15))
e2 = Label(root, text=eng(data[x][0]),font=tkinter.font.Font(family="Arial", size=15))

c1 = Label(root, text='中文：', font=tkinter.font.Font(family="Arial", size=15))
c2 = Label(root, text=data[x][1],font=tkinter.font.Font(family="Arial", size=15))
textbox1 = Entry(root, textvariable=ans)

b = Button(root, text='next', command=run)
sc = Label(root, text=f'分數: {score}',font=tkinter.font.Font(family="Arial", size=15))

e1.grid(row=0, column=0)
e2.grid(row=0, column=2)
c1.grid(row=2, column=0)
c2.grid(row=2, column=2)
textbox1.grid(row=3, column=0, columnspan=3)
sc.grid(row=8, column=0, columnspan=3)
b.grid(row=10, column=0, columnspan=3)

root.mainloop()
