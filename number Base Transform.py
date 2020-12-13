print("pls input a number : ",end="")
data=input()
data_int=int(data)

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

    for q in range(0,len(out_data)):
        if(out_data[q]=='10'):
            out_data[q]='A'
        if(out_data[q]=='11'):
            out_data[q]='B'
        if(out_data[q]=='12'):
            out_data[q]='C'
        if(out_data[q]=='13'):
            out_data[q]='D'
        if(out_data[q]=='14'):
            out_data[q]='E'
        if(out_data[q]=='15'):
            out_data[q]='F'

    for r in range(0,len(out_data)):
        out+=out_data[r]
    return out

print("bin base :"+tran_base(data_int,2))
print("oct base :"+tran_base(data_int,8))
print("hex base :"+tran_base(data_int,16))
