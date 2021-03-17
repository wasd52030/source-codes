x=[1,8,4,9,25,10,36,97,15,23]


for j in range(0,len(x)):
    for i in range(0,len(x)-1):
        if x[i]>x[i+1]:
            x[i],x[i+1]=x[i+1],x[i]


print(x)
