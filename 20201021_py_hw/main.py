f1=open("input.txt","r")
data=[]
a=-1
c1=-1;
c2="";
word=['$','@','#','%','&']
for x in f1:
    data.append(int(x))


while True:
    if a==len(data):
        break
    else:
        a+=1
    
    try:
        for v in range(data[a]):
            for j in range(data[a]-v-1):
                print(' ',end='')
            for i in range(v+1):
                c1+=1
                c2=word[c1%5]
                print(c2,end='')
            print('\n',end='')
        c1=-1
    except:
        pass
    
    
    