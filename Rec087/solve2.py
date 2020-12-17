#迴圈解
def calc(n):
    out=2
    for i in range(2,n+1):
        out+=i
    return out

k=0
while True:
    print("Please input a non-negative number: ",end="")
    k=int(input())
    if k<0:
        break
    else:
        print("The maximum number of cakes: %d"%calc(k))