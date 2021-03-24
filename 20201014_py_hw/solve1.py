import time
f1=open("input.txt","r")
x=[]
y=[]

for i in f1:
    x.append(int(i))
f1.close()

#將原本的資料串列應要求切成兩數一組的二維串列
for i in range(0,len(x),2):
    y.append(x[i:i+2])

print(x)
#print(len(y[0]))

for a in range(0,len(y)):
    for b in range(0,len(y[0])-1):
        if y[a][b]<y[a][b+1]:
            for i in range(y[a][b],y[a][b+1]+1):
                print(str(i)+" ",end="")
            print()
        if y[a][b]>y[a][b+1]:
            for i in range(y[a][b+1],y[a][b]+1):
                print(str(i)+" ",end="")
            print()