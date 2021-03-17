from tkinter import *

root=Tk()
s=""
x=Label(root,text=s,width=48,height=3).grid(row=0,columnspan=3)

def clear():
    global s
    s=""
    Label(root,text=s,width=48,height=3).grid(row=0,columnspan=3)

def x():
    global s
    s+="/"
    Label(root,text=s,width=48,height=3).grid(row=0,columnspan=3)

def y():
    global s
    s+="*"
    Label(root,text=s,width=48,height=3).grid(row=0,columnspan=3)

def a():
    global s
    s+="-"
    Label(root,text=s,width=48,height=3).grid(row=0,columnspan=3)

def b():
    global s
    s+="+"
    Label(root,text=s,width=48,height=3).grid(row=0,columnspan=3)

def dt():
    global s
    s+="."
    Label(root,text=s,width=48,height=3).grid(row=0,columnspan=3)

def q():
    global s
    s+="7"
    Label(root,text=s,width=48,height=3).grid(row=0,columnspan=3)

def w():
    global s
    s+="8"
    Label(root,text=s,width=48,height=3).grid(row=0,columnspan=3)

def e():
    global s
    s+="9"
    Label(root,text=s,width=48,height=3).grid(row=0,columnspan=3)

def qq():
    global s
    s+="4"
    Label(root,text=s,width=48,height=3).grid(row=0,columnspan=3)

def ww():
    global s
    s+="5"
    Label(root,text=s,width=48,height=3).grid(row=0,columnspan=3)

def ee():
    global s
    s+="6"
    Label(root,text=s,width=48,height=3).grid(row=0,columnspan=3)

def qqq():
    global s
    s+="1"
    Label(root,text=s,width=48,height=3).grid(row=0,columnspan=3)

def www():
    global s
    s+="2"
    Label(root,text=s,width=48,height=3).grid(row=0,columnspan=3)

def eee():
    global s
    s+="3"
    Label(root,text=s,width=48,height=3).grid(row=0,columnspan=3)

def qqqq():
    global s
    s+="0"
    Label(root,text=s,width=48,height=3).grid(row=0,columnspan=3)

def eq():
    global s
    s=str(eval(s))
    Label(root,text=s,width=48,height=3).grid(row=0,columnspan=3)

Button(root,text='C',width=48,height=3,command=clear).grid(row=1,columnspan=3)
Button(root,text='/',width=15,height=3,command=x).grid(row=1,column=3)
Button(root,text='7',width=15,height=3,command=q).grid(row=2,column=0)
Button(root,text='8',width=15,height=3,command=w).grid(row=2,column=1)
Button(root,text='9',width=15,height=3,command=e).grid(row=2,column=2)
Button(root,text='*',width=15,height=3,command=y).grid(row=2,column=3)
Button(root,text='4',width=15,height=3,command=qq).grid(row=3,column=0)
Button(root,text='5',width=15,height=3,command=ww).grid(row=3,column=1)
Button(root,text='6',width=15,height=3,command=ee).grid(row=3,column=2)
Button(root,text='-',width=15,height=3,command=a).grid(row=3,column=3)
Button(root,text='1',width=15,height=3,command=qqq).grid(row=4,column=0)
Button(root,text='2',width=15,height=3,command=www).grid(row=4,column=1)
Button(root,text='3',width=15,height=3,command=eee).grid(row=4,column=2)
Button(root,text='+',width=15,height=3,command=b).grid(row=4,column=3)
Button(root,text='0',width=32,height=3,command=qqqq).grid(row=5,columnspan=2)
Button(root,text='.',width=15,height=3,command=dt).grid(row=5,column=2)
Button(root,text='=',width=15,height=3,command=eq).grid(row=5,column=3)

root.mainloop()