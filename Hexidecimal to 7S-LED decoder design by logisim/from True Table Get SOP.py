data=[1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,0] #函數輸出真值表
out=[]

for x in range(0,len(data)):
    if data[x]==1:
        out.append(x)

print("SOP LIST:",end="")
print(out)
