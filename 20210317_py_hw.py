from tkinter import *
import tkinter.messagebox
import random
import time

root=Tk()
root.resizable(0,0)

n=x=0

a=[]
k=[0,1,2,3,4,5,6,7,8,9]
random.shuffle(k)
for i in range(1,19):
    w=random.sample(k,1)
    a.append(w[0])
    a.append(w[0])
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
    
    if n==len(btns)/2:
        t2=time.time()
        tkinter.messagebox.showwarning('title','共用%d秒'%(t2-t1))

root.mainloop()