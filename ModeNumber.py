import random
def find(data):
    cnt_num={}
    for i in data:
        if i in cnt_num:
            cnt_num[i]+=1
        else:
            cnt_num[i]=1

    nmax=[]
    for g in cnt_num.values():
        nmax.append(g)
    flag=max(nmax)

    if flag!=1:
        for k,v in cnt_num.items():
            if v==flag:
                print('眾數:%d , 重數:%d\n'%(k,v),end="")
    else:
        print("無眾數")
                
#列表推導式 ==> [表示式 for 疊代變數 in 可疊代物件 if 條件表示式]
#其中「if 條件表示式」為可選項，需要再用即可
a=[random.randint(1,100) for i in range(50)]
a.sort()
print(a)
print("a有%d個元素"%len(a))
find(a)