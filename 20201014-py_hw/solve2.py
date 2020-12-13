import numpy

data=[]
calc=numpy.array([0,0])

with open('input.txt','r') as f1:
    for k in f1:
        data.append(int(k))

print(data)

datacounter=0 #data串列計數器
calccounter=0 #calc陣列計數器
while datacounter<=len(data):
    try:
        calc[calccounter]=data[datacounter]
        calccounter+=1
    except IndexError:
        calccounter=0#初始化陣列計數器

        #先檢查datacounter是否小於len(data)
        #再減一以方便讓被try-except略過的數字進入下一輪
        if datacounter<len(data):
            datacounter-=1

        #題目要求從最小的數字印到最大的數字，直接對陣列排序再用for去印即可
        calc.sort()
        for i in range(calc[0],calc[1]+1):
            print("%d "%i,end="")
        print()
    datacounter+=1