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
                

a=[ 1, 3, 3, 3, 3, 4, 4, 6, 7, 11, 11, 11, 12, 14, 14, 14, 15, 16, 18, 18, 
    22, 23, 24, 25, 25, 26, 26, 26, 27, 27, 28, 28, 30, 31, 31, 32, 33, 33, 
    34, 38, 39, 41, 41, 41, 42, 42, 45, 45, 47, 47, 50, 54, 54, 55, 55, 56, 
    56, 58, 59, 60, 61, 62, 62, 64, 66, 67, 68, 69, 69, 70, 70, 73, 75, 75, 
    83, 84, 85, 86, 87, 87, 87, 88, 89, 89, 89, 89, 89, 90, 92, 93, 93, 94, 
    95, 96, 96, 97, 99, 100, 100, 100]
print("a有%d個元素"%len(a))
find(a)