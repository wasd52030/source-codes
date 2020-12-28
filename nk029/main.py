q=input()
data=input().split()
cnt={}

for k in data:
    d=[]
    for x in range(len(k)):
        d.append(int(k[x]))
        
    sum=0
    for a in d:
        sum+=a
    cnt[int(k)]=sum
    
    
q=[]
for k,v in cnt.items():
    c=[]
    c.append(k)
    c.append(v)
    q.append(c)

q.sort(key=lambda x:x[1])
for g in range(len(q)-1):
    if q[g][1]==q[g+1][1]:
        if q[g]>q[g+1]:
            q[g+1],q[g]=q[g],q[g+1] #python swap -> a,b=b,a


for a in range(len(q)):
    print(str(q[a][0])+" ",end="")
