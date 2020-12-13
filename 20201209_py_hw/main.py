import os
from random import sample
import time
data=[]
g=[]
with open('eng.txt','r') as f1:
    for k in f1:
        data.append(f1.readline().strip())

print("輸入1開始遊戲...",end="")
kin1=int(input())
if(kin1==1):
    while True:
        print("輸入要練幾個單字 : ",end="")
        words=int(input())
        t1=time.time()
        g=sample(data,words)
        gc=0
        while True:
            if gc>=len(g):
                t2=time.time()
                print('共用了 : %f s'%(t2-t1))
                break
            else:
                print(g[gc])
                gin=input()
                if(gin==g[gc]):
                    print()
                    gc+=1
                else:
                    print()



