import random
from tkinter import *
import tkinter.font

root = Tk()

# 表單區塊
DataForm = Frame(root)
DataForm.grid(row=0, column=0)

# 按鈕(功能)區塊
FuncForm = Frame(root)
FuncForm.grid(row=1, column=0)

sid = StringVar()
name = StringVar()
department = StringVar()
address = StringVar()
phone = StringVar()
sex = IntVar()
f = tkinter.font.Font(family="Arial", size=15)
d = []
sexs = ['男', '女']
cnt = 0
DataModels = []


class data:
    def __init__(self, id, name, sex, depart, address, phone):
        self.id = id
        self.name = name
        self.sex = sex
        self.depart = depart
        self.address = address
        self.phone = phone


def readall():
    global d, DataModels
    d, DataModels = [], []
    with open('./d.txt', 'r', encoding='utf-8') as f1:
        d = [i.split() for i in f1]

    for i in d:
        a = data(i[0], i[1], i[2], i[3], i[4], i[5])
        DataModels.append(a)


def SetFormData():
    sid.set(d[cnt][0])
    name.set(d[cnt][1])
    sex.set(1) if d[cnt][2] == "男" else sex.set(2)
    department.set(d[cnt][3])
    address.set(d[cnt][4])
    phone.set(d[cnt][5])

def front():
    global cnt
    if cnt > 0:
        cnt -= 1
        SetFormData()

def back():
    global cnt, d
    if cnt < len(d)-1:
        cnt += 1
        SetFormData()

def clf():
    sid.set('')
    name.set('')
    sex.set(0)
    department.set('')
    address.set('')
    phone.set('')

def write():
    global DataModels
    f = open('./d.txt', 'w', encoding='utf-8')
    for i in DataModels:
        f.write(f'{i.id} {i.name} {i.sex} {i.depart} {i.address} {i.phone}\n')
    f.close()

def dl():
    global DataModels, cnt
    id = sid.get()
    for index, item in enumerate(DataModels):
        if id == item.id:
            if index == len(DataModels)-1:
                cnt -= 1
            del(DataModels[index])
            write()
            readall()
            SetFormData()
            break

def upe():
    global DataModels, cnt,d
    id = sid.get()
    s = '男' if sex.get() == 1 else '女'
    a = data(sid.get(), name.get(), s, department.get(), address.get(), phone.get())
    if id in [i.id for i in DataModels]:
        DataModels[cnt]=a
        write()
        readall()
        SetFormData()
    else:
        DataModels.append(a)
        write()
        readall()
        cnt = len(DataModels)-1
        SetFormData()

Label(DataForm, text='學號：', font=f).grid(row=0, column=0)
Entry(DataForm, textvariable=sid).grid(row=0, column=1)

Label(DataForm, text='姓名：', font=f).grid(row=1, column=0)
Entry(DataForm, textvariable=name).grid(row=1, column=1)

for i in range(2):
    Radiobutton(DataForm, text=sexs[i], variable=sex, value=i+1, font=f).grid(row=2, column=i)

Label(DataForm, text='系所：', font=f).grid(row=3, column=0)
Entry(DataForm, textvariable=department).grid(row=3, column=1)

Label(DataForm, text='地址：', font=f).grid(row=4, column=0)
Entry(DataForm, textvariable=address).grid(row=4, column=1)

Label(DataForm, text='電話：', font=f).grid(row=5, column=0)
Entry(DataForm, textvariable=phone).grid(row=5, column=1)

ft = Button(FuncForm, text="<<", font=f, command=front)
ft.grid(row=6, column=0)

ude = Button(FuncForm, text="更新", font=f, command=upe)
ude.grid(row=6, column=1)

dl = Button(FuncForm, text="刪除", font=f, command=dl)
dl.grid(row=6, column=2)

nw = Button(FuncForm, text="新增", font=f, command=clf)
nw.grid(row=6, column=3)

nx = Button(FuncForm, text=">>", font=f, command=back)
nx.grid(row=6, column=4)

readall()
SetFormData()
root.mainloop()
