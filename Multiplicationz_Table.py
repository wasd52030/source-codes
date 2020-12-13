a=1
b=1
while True:
    print("%d*%d=%d\t"%(a,b,a*b),end="")
    b+=1
    if b>9:
        b=1
        a+=1
        print()
    
    if a==10:
        break
