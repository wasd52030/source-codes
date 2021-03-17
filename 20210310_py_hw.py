from tkinter import *
import tkinter.messagebox
import re

root=Tk()
root.resizable(0,0)

r=0
btn_txt=['7','8','9','*','4','5','6','-','1','2','3','+']
s="0"

def clear():
    global s
    s="0"
    x['text']=s

def run(g):
    global s
    if s=="0":
        s=g
    else:
        s+=g
    x['text']=s

def calc():
    global s
    if re.match('^\d.*$',s) or re.match('^-\d.*$',s):
        s=str(eval(s))
    else:
        tkinter.messagebox.showwarning('','輸入錯誤，將重設為0')
        s="0"
    x['text']=s

x=Label(root,text=s,borderwidth=1,relief="solid",width=65,height=3)
x.grid(row=0,columnspan=4)

C=Button(root,text='C',width=48,height=3,command=clear)
C.grid(row=1,column=0,columnspan=3)

dev=Button(root,text='/',width=15,height=3,command=lambda n='/':run(n))
dev.grid(row=1,column=3)

zero=Button(root,text='0',width=31,height=3,command=lambda n='0':run(n))
zero.grid(row=5,columnspan=2)

dot=Button(root,text='.',width=15,height=3,command=lambda n='.':run(n))
dot.grid(row=5,column=2)

eq=Button(root,text='=',width=15,height=3,command=calc)
eq.grid(row=5,column=3)

for i in range(2,5):
    for j in range(0,4):
        b=Button(root,text=btn_txt[r],width=15,height=3,command=lambda n=btn_txt[r]:run(n))
        b.grid(row=i,column=j)
        r+=1

root.mainloop()