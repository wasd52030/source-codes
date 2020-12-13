import numpy

data=[]
calc=numpy.array([0,0,0])
with open('input.txt','r') as f1:
    for line in f1:
        for x in line.split():
            data.append(int(x))

datacounter=0
calccounter=0
isTri=0
NoTri=0
while datacounter<=len(data):
    try:
        calc[calccounter]=data[datacounter]
        calccounter+=1
    except IndexError:
        #先對calc排序，這樣一來，只要檢查比較小的兩個數字的和是否大於最大值即可判斷是否為三角形了
        calc.sort()
        out=""
        
        # a=calc[0] b=calc[1] c=calc[2]
        a=b=c=0
        for k in range(0,len(calc)):
            if k==0:
                a=calc[k]
            elif k==1:
                b=calc[k]
            elif k==2:
                c=calc[k]

        for k in calc:
            out+=str(k)+" "

        if a+b>c:
            out+="是三角形"
            isTri+=1
        else:
            out+="不是三角形"
            NoTri+=1

        print(out)

        calccounter=0 #初始化陣列計數器

        #先檢查datacounter是否小於len(data)
        #再減一以方便讓被try-except略過的數字進入下一輪
        if datacounter<len(data): 
            datacounter-=1
    datacounter+=1
print("True: %d\nFalse: %d"%(isTri,NoTri),end="")