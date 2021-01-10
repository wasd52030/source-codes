out_data=[]
def tran_base(x,y):
    if x==0:
        out_data.reverse()
        out=""       
        hexs=[]
        for i in range(65,91): #A的ascii=65 Z的ascii=90
            hexs.append(chr(i))
            
        for i in range(0,len(out_data)):
            if out_data[i]>=10 and out_data[i]<=36:
                out_data[i]=hexs[out_data[i]-10]

        for k in out_data:
            out+=str(k)
        out_data.clear()
        return out
    else:
        out_data.append(x%y)
        return tran_base(int(x/y),y)

while True:
    x,y=input().split()
    if int(x)<=1 or int(y)<=1:
        break
    else:
        print(tran_base(int(x),int(y)))