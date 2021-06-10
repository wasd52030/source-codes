from tkinter import *
import math

root = Tk()

with open('input.txt') as f1:
    in_data = [k for k in f1]

d = [math.comb(i-1, j-1) for i in range(1, int(in_data[0])+2) for j in range(1, i+1)]
cnt = 0
f = True

for i in range(1, int(in_data[0])+2):
    for j in range(1, (int(in_data[0])+2)-i+1):
        Label(root).grid(row=i, column=j)
    for k in range(1, 2*i-1):
        r = k+j-1
        f = not f
        if f == True:
            Label(root, text=d[cnt]).grid(row=i, column=r)
            cnt += 1
        else:
            Label(root).grid(row=i, column=r+1)

root.mainloop()
