from tkinter import *
import tkinter.messagebox
import random
import time
import sys

root=Tk()
root.resizable(0,0)

n=x=0
a=[]
ans=[]
btn_no=[]
btns=[]
t1=t2=time.time()

def numlist_init():
    k=[0,1,2,3,4,5,6,7,8,9]
    g=[]
    random.shuffle(k)
    for i in range(1,19):
        w=random.sample(k,1)
        g.append(w[0])
        g.append(w[0])
    random.shuffle(g)
    return g

def gamedata_init():
    ans.clear()
    btn_no.clear()

def game_window_init():
    global a,x
    a=numlist_init()
    for i in range(0,6):
        for j in range(0,6):
            b=Button(root,text=a[x],width=10,height=2,command=lambda c=a[x],id=x:run(c,id))
            b.grid(row=i,column=j)
            btns.append(b)
            x+=1

def run(Xans,Xid):
    global n,x,t1,t2,a,ans,btn_no,btns

    if n==0:
        t1=time.time()

    ans.append(Xans)
    btn_no.append(Xid)
    btns[btn_no[0]]['state']='disable'

    if len(ans)==2:
        if ans[0]==ans[1]:
            btns[btn_no[1]]['state']='disable'
            n+=1
        else:
            btns[btn_no[0]]['state']='normal'
        gamedata_init()

    if n==len(btns)/2:
        t2=time.time()
        restart=tkinter.messagebox.showwarning('title','共用%d秒\n要重新開始嗎'%(t2-t1),type=tkinter.messagebox.YESNO)
        n=x=0
        btns.clear()
        a.clear()
        if restart=="yes":
            game_window_init()
        else:
            sys.exit(0)


def main():
    game_window_init()
    root.mainloop()

main()