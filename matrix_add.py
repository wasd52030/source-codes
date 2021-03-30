#矩陣相加

def matrix_init(k):
    i=0
    A=[]
    while True:
        if i<k[0]:
            c=[int(a) for a in input(f'輸入矩陣數值第{i+1}列為:').split(' ')]
            if len(c)!=k[1]:
                print('輸入錯誤，請重新輸入')
                continue
            i+=1
            A.append(c)
        else:
            return A
            break

def matrix_add(a,b):
    mlen=[len(a),len(a[0]),len(b),len(b[0])]
    result=[]
    if mlen[0]!=mlen[2] or mlen[1]!=mlen[3]:
        print('無法相加')
    else:
        for i in range(len(a)):
            k=[]
            for j in range(len(a[0])):
                k.append(a[i][j]+b[i][j])
            result.append(k)
    return result

a=[int(a) for a in input('表示第1個矩陣為:').split(' ')]
A=matrix_init(a)

b=[int(a) for a in input('表示第2個矩陣為:').split(' ')]
B=matrix_init(b)

final=matrix_add(A,B)

for i in range(len(final)):
    for j in range(len(final)):
        print(f'{final[i][j]} ',end='')
    print()