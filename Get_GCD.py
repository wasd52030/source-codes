print("1st num=",end="")
x=input()
print("2nd num=",end="")
y=input()
CommonFactor=[] #公因數表
c=0

while True:
    c+=1
    if float(x)%c == 0 and float(y)%c==0:
        CommonFactor.append(c)
    
    if c>float(x) or c>float(y):
        break

print(max(CommonFactor))