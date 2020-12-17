#遞迴解
def calc(n):
    if n==1:
        return 2
    else:
        return n+calc(n-1)


k=0
while True:
    print("Please input a non-negative number: ",end="")
    k=int(input())
    if k<0:
        break
    else:
        print("The maximum number of cakes: %d"%calc(k))