from tkinter import *
import math

root=Tk()
root.title("BSK TRA")
in_data=[]
num_data=[]

with open('input.txt') as f1:
    for k in f1:
        in_data.append(k)

p=0
for i in range(0,int(in_data[0])+1):
    for j in range(0,int(in_data[0])+1):
        if i==0 and j==1:
            continue
        else:
            p=math.comb(i,j)   #計算nCr(i,j)，python3.8以上始可使用
            if p>0:
                num_data.append(p)

x=0
out=""
for i in range(int(in_data[0])+1):
    for k in range(int(in_data[0])+1,i+1,-1):
        out+=" "
    for j in range(0,i+1):
        out+=" {} ".format(num_data[x])
        #out+="  %d  "%(num_data[x])
        x+=1
    out+="  "
    out+="\n"

o=Label(root,text=out,font=('Arial',16)).pack()

root.mainloop()