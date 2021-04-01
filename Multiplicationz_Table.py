a=1
b=1
while True:
    print("%d*%d=%d\t"%(a,b,a*b),end="")
    a+=1
    if a>9:
        a=1
        b+=1
        print()
    
    if b==10:
        break
