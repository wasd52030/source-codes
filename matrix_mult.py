#矩陣相乘

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

def matrix_mult(a,b):
    mlen=[len(a),len(a[0]),len(b),len(b[0])]
    result=[]
    if mlen[1]!=mlen[2]:
        print('無法相乘')
    else:
        for i in range(len(a)):
            n=[]
            for j in range(len(b[0])):
                x,y=0,0
                for k in range(len(b)):
                    x=a[i][k]*b[k][j]
                    y+=x
                n.append(y)
            result.append(n)
    return result

a=[int(a) for a in input('表示第1個矩陣為:').split(' ')]
A=matrix_init(a)

b=[int(a) for a in input('表示第2個矩陣為:').split(' ')]
B=matrix_init(b)

final=matrix_mult(A,B)

for i in range(len(final)):
    print(*final[i])