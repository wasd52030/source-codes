from tkinter import *
import math

root=Tk()
in_data=[]

with open('input.txt') as f1:
    in_data=[k for k in f1]

out=""
for i in range(1,int(in_data[0])+2):
    for k in range(int(in_data[0])+1,i+1,-1):
        out+=" "
    for j in range(1,i+1):
        out+=" {} ".format(math.comb(i-1,j-1))
    out+="  "
    out+="\n"

Label(root,text=out,font=('Arial',16)).pack()

root.mainloop()