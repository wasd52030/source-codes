from tkinter import *
root=Tk()
root.title("BSK TRA")

in_data=[]
num_data=[]
with open('input.txt') as f1:
    for k in f1:
        in_data.append(k)

def factorial(x):
    g=1
    for i in range(1,x+1):
        g*=i
    if x==0:
        g=1
    return g

def nCr(n,r):
    return (factorial(n))//(factorial(n-r)*factorial(r))

p=0
for i in range(0,int(in_data[0])+1):
    for j in range(0,int(in_data[0])+1):
        if i==0 and j==1:
            continue
        else:
            p=nCr(i,j)
            if p>0:
                num_data.append(p)

x=0
out=""
for i in range(int(in_data[0])+1):
    for k in range(int(in_data[0])+1,i+1,-1):
        out+=" "
    for j in range(0,i+1):
        out+="  {}  ".format(num_data[x])
        #out+="  %d  "%(num_data[x])
        x+=1
    out+="  "
    out+="\n"

o=Label(root,text=out).pack()

root.mainloop()