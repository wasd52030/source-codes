import collections

a=int(input())
in_num=a
b=2
PrimeFactor=[]
out=str(in_num)+"="


#b=2,3,4...如果a可以整除b，就把b加入質因數表裡面，並且讓a=a/b，直至無法整除
#應該類似於短除法
while a>1:
    while a%b==0:
        PrimeFactor.append(b)
        a/=b
    b+=1

#求每個質因數的次方，並放到Dictionary中，類似於java的map
#collections.Counter(List) 可用來求List中元素重複的次數，並放到一字典裏面
PrimePow=collections.Counter(PrimeFactor)

for i in PrimePow:
    if PrimePow[i] != 1:
        out+=str(i)+"^"+str(PrimePow[i])+"*"
    else:
        out+=str(i)+"*"

out=out[:-1]


for i in PrimeFactor:
    if i==in_num:
        out=str(i)+"是質數"

print(out)