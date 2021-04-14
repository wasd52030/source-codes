x=[6,5,9,2,7,8]
w=0

for j in range(0,len(x)):
    for i in range(0,len(x)-1):
        if x[i]>x[i+1]:
            x[i],x[i+1]=x[i+1],x[i]

print(x)