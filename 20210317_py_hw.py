from tkinter import *
import tkinter.messagebox
import random
import time

root=Tk()
root.resizable(0,0)
n=0
x=0
a=[0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,0,0,9,9,8,8,7,7,6,6,5,5,4,4,3,3]
random.shuffle(a)
ans=[]
btn_no=[]
btns=[]
t1=t2=time.time()

for i in range(0,6):
    for j in range(0,6):
        b=Button(root,text=a[x],width=10,height=2,command=lambda c=a[x],id=x:run(c,id))
        b.grid(row=i,column=j)
        btns.append(b)
        x+=1

def run(x,y):
    global n,t1,t2

    if n==0:
        t1=time.time()

    ans.append(x)
    btn_no.append(y)
    btns[btn_no[0]]['state']='disable'
    if len(ans)==2:
        if ans[0]==ans[1]:
            btns[btn_no[1]]['state']='disable'
            n+=1
        else:
            btns[btn_no[0]]['state']='normal'
        ans.clear()
        btn_no.clear()
    print(n)
    if n==len(btns)/2:
        t2=time.time()
        tkinter.messagebox.showwarning('title','共用%d秒'%(t2-t1))

root.mainloop()