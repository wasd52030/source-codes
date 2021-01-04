def tran_base(x,y):
    a=0
    b=0
    out_data=[]
    out=""
    while True:
        a=x%y
        b=x/y
        x=int(b)
        out_data.append(str(int(a)))
        if int(b)==0 and a==0 :
            out_data.reverse()
            out_data.pop(0)
            break
            
    hexs={}  #對10以上的數字建立數字跟字母的對照表
    x=0
    for i in range(10,36):
        hexs[str(i)]=str(chr(65+x))
        x+=1

    for q in range(0,len(out_data)):
        if str(out_data[q]) in hexs:
            out_data[q]=hexs[str(out_data[q])]

    for r in range(0,len(out_data)):
        out+=out_data[r]
    return out

while True:
    x,y=input().split()
    if int(x)<=1 or int(y)<=1:
        break
    else:
        print(tran_base(int(x),int(y)))