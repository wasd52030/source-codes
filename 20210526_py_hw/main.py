import random
from tkinter import *
import tkinter.font

root = Tk()

with open('./d.txt', 'r', encoding='utf-8') as f1:
    d = [i.split() for i in f1]

sid = StringVar()
name = StringVar()
department = StringVar()
address = StringVar()
phone = StringVar()
sex = IntVar()
f = tkinter.font.Font(family="Arial", size=15)
sexs = ['男', '女']
cnt = 0

def setdata():
    sid.set(d[cnt][0])
    name.set(d[cnt][1])
    department.set(d[cnt][3])
    sex.set(1) if d[cnt][2] == "男" else sex.set(2)
    address.set(d[cnt][4])
    phone.set(d[cnt][5])

def front():
    global cnt
    if cnt>0:
        cnt-=1
        setdata()

def back():
    global cnt,d
    if cnt<len(d)-1:
        cnt+=1
        setdata()

Label(root, width=15, text='學號：', font=f).grid(row=0, column=0)
Entry(root, textvariable=sid).grid(row=0, column=1)

Label(root, width=15, text='姓名：', font=f).grid(row=1, column=0)
Entry(root, textvariable=name).grid(row=1, column=1)

for i in range(2):
    Radiobutton(root, text=sexs[i], variable=sex, value=i+1, font=f).grid(row=2, column=i)

Label(root, width=15, text='系所：', font=f).grid(row=3, column=0)
Entry(root, textvariable=department).grid(row=3, column=1)

Label(root, width=15, text='地址：', font=f).grid(row=4, column=0)
Entry(root, textvariable=address).grid(row=4, column=1)

Label(root, width=15, text='電話：', font=f).grid(row=5, column=0)
Entry(root, textvariable=phone).grid(row=5, column=1)

u = Button(root, width=15, text="上一筆", font=f,command=front)
u.grid(row=6, column=0)

v = Button(root, width=15, text="下一筆", font=f,command=back)
v.grid(row=6, column=1)

setdata()
root.mainloop()