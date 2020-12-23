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
            out_data[q]='G'
        if(out_data[q]=='16'):
            out_data[q]='H'
        if(out_data[q]=='17'):
            out_data[q]='I'
        if(out_data[q]=='18'):
            out_data[q]='J'
        if(out_data[q]=='19'):
            out_data[q]='K'
        if(out_data[q]=='20'):
            out_data[q]='L'
        if(out_data[q]=='21'):
            out_data[q]='B'
        if(out_data[q]=='22'):
            out_data[q]='M'
        if(out_data[q]=='23'):
            out_data[q]='N'
        if(out_data[q]=='24'):
            out_data[q]='O'
        if(out_data[q]=='25'):
            out_data[q]='P'
        if(out_data[q]=='26'):
            out_data[q]='Q'
        if(out_data[q]=='27'):
            out_data[q]='R'
        if(out_data[q]=='28'):
            out_data[q]='S'
        if(out_data[q]=='29'):
            out_data[q]='T'
        if(out_data[q]=='30'):
            out_data[q]='U'
        if(out_data[q]=='31'):
            out_data[q]='V'
        if(out_data[q]=='32'):
            out_data[q]='W'
        if(out_data[q]=='33'):
            out_data[q]='X'
        if(out_data[q]=='34'):
            out_data[q]='Y'
        if(out_data[q]=='35'):
            out_data[q]='Z'

    for r in range(0,len(out_data)):
        out+=out_data[r]
    return out

while True:
    x,y=input().split()
    if int(x)<=1 or int(y)<=1:
        break
    else:
        print(tran_base(int(x),int(y)))
        pass