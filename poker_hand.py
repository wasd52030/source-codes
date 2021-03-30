#撲克遊戲
#S->黑桃 H->愛心 D->方塊 C->梅花

p1=[]
p2=[]

def judgment(g):
    h={}
    n={}
    pairs=[0 for i in range(3)] #四同點、三同點、兩同點
    for i in range(len(g)):
        if g[i][0] in h:
            h[g[i][0]]+=1
        else:
            h[g[i][0]]=1
        if g[i][1] in n:
            n[g[i][1]]+=1
        else:
            n[g[i][1]]=1

    Flush='' #同花
    for k,v in h.items():
        if v==5:
            Flush=k

    Straight=0 #順子
    for i in range(len(g)-2,-1,-1):
        if abs(int(g[i+1][1])-int(g[i][1]))==1 or abs(int(g[i+1][1])-int(g[i][1]))==12:
            Straight+=1
    
    for k,v in n.items():
        if v==4:
            pairs[0]+=1
        elif v==3:
            pairs[1]+=1
        elif v==2:
            pairs[2]+=1

    #同花順:8 四條:7 葫蘆:6 同花:5 順子:4 三條:3 兩對:2 一對:1 散牌:0
    if Flush!='' and Straight==4:
        return 8
    elif pairs[0]==1:
        return 7
    elif pairs[1]==1 and pairs[2]==1:
        return 6
    elif Flush!='':
        return 5
    elif Straight==4:
        return 4
    elif pairs[1]==1:
        return 3
    elif pairs[2]==2:
        return 2
    elif pairs[2]==1:
        return 1
    else:
        return 0

def d_input():
    g=[[n[0:1],n[1:]] for n in input().split(' ')]
    return g

def player():
    global p1,p2
    print('S->黑桃 H->愛心 D->方塊 C->梅花')
    p1=d_input()
    p2=d_input()

def result(p1,p2):
    #print('同花順:8 四條:7 葫蘆:6 同花:5 順子:4 三條:3 兩對:2 一對:1 散牌:0')
    #print(f'Player1=>{judgment(p1)} Player2=>{judgment(p2)}')
    if judgment(p1)>judgment(p2):
        print('\n1\n')
    else:
        print('\n0\n')

while True:
    e=''
    player()
    e=int(input())
    result(p1,p2)
    if e==-1:
        break
    elif e==0:
        continue