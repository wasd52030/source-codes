import math
f1=open("in.txt","r")
f2=open("out.txt","w",encoding="utf-8")
Data=[]
sum=odd=even=0

def Isinteger(n):
    return math.ceil(n) == math.floor(n)

for x in f1:
    Data.append(float(x))

Data.sort()
print("輸入資料經排序後 : " + str(Data),file=f2)

for i in range(0,len(Data)):
    sum+=Data[i]
    if Isinteger(Data[i]):
        if Data[i]%2==0:
            even+=1
        else:
            odd+=1

max=max(Data)
min=min(Data)
avg=sum/len(Data)

print("最大值 : "+str(max)+"\n"+"最小值 : "+str(min)+"\n"+"平均值 : "+str(avg)+"\n"+"奇數有"+str(odd)+"個\n"+"偶數有"+str(even)+"個\n",file=f2)
print("資料分析完畢")

f1.close()
f2.close()