#轉置矩陣

k=[int(a) for a in input('輸入N及M為:').split(' ')]
A=[]
B=[]

i=0
while True:
    if i<k[0]:
        c=[int(a) for a in input(f'輸入矩陣數值第{i+1}列為:').split(' ')]
        if len(c)!=k[1]:
            print('輸入錯誤，請重新輸入')
            continue
        i+=1
        A.append(c)
    else:
        break

for i in range(len(A[0])):
    g=[]
    for j in range(len(A)):
        g.append(A[j][i])
    B.append(g)

for i in range(len(B)):
    s=''
    for n in B[i]:
        s+=f'{n} '
    print(f'輸出矩陣第{i+1}列為{s}')