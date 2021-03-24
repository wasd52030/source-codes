from tkinter import *

root=Tk()
s="由O開始"
btns=[]
game_data=[]
player_flag=True
win_flag=False
n=0

x=Label(root,text=s,borderwidth=1,relief="solid",width=49,height=3)
x.grid(row=0,columnspan=3)

def run(btnid):
    global player_flag,s,win_flag
    f=""
    c=0
    if player_flag==True:
        f='O'
        s="現在是X"
        btns[btnid]['text']=f
        x['text']=s
    else:
        f='X'
        s="現在是O"
        btns[btnid]['text']=f
        x['text']=s

    if btns[0]['text']=="O" and btns[1]['text']=="O" and btns[2]['text']=="O":
        s="O獲勝"
        x['text']=s
        win_flag=True
        for i in btns:
            i['state']='disable'
    elif btns[3]['text']=="O" and btns[4]['text']=="O" and btns[5]['text']=="O":
        s="O獲勝"
        x['text']=s
        win_flag=True
        for i in btns:
            i['state']='disable'
    elif btns[6]['text']=="O" and btns[7]['text']=="O" and btns[8]['text']=="O":
        s="O獲勝"
        x['text']=s
        win_flag=True
        for i in btns:
            i['state']='disable'
    elif btns[0]['text']=="O" and btns[4]['text']=="O" and btns[8]['text']=="O":
        s="O獲勝"
        x['text']=s
        win_flag=True
        for i in btns:
            i['state']='disable'
    elif btns[2]['text']=="O" and btns[4]['text']=="O" and btns[6]['text']=="O":
        s="O獲勝"
        x['text']=s
        win_flag=True
        for i in btns:
            i['state']='disable'
    elif btns[0]['text']=="O" and btns[3]['text']=="O" and btns[6]['text']=="O":
        s="O獲勝"
        x['text']=s
        win_flag=True
        for i in btns:
            i['state']='disable'
    elif btns[1]['text']=="O" and btns[4]['text']=="O" and btns[7]['text']=="O":
        s="O獲勝"
        x['text']=s
        win_flag=True
        for i in btns:
            i['state']='disable'
    elif btns[2]['text']=="O" and btns[5]['text']=="O" and btns[8]['text']=="O":
        s="O獲勝"
        x['text']=s
        win_flag=True
        for i in btns:
            i['state']='disable'

    if btns[0]['text']=="X" and btns[1]['text']=="X" and btns[2]['text']=="X":
        s="X獲勝"
        x['text']=s
        win_flag=True
        for i in btns:
            i['state']='disable'
    elif btns[3]['text']=="X" and btns[4]['text']=="X" and btns[5]['text']=="X":
        s="X獲勝"
        x['text']=s
        win_flag=True
        for i in btns:
            i['state']='disable'
    elif btns[6]['text']=="X" and btns[7]['text']=="X" and btns[8]['text']=="X":
        s="X獲勝"
        x['text']=s
        win_flag=True
        for i in btns:
            i['state']='disable'
    elif btns[0]['text']=="X" and btns[4]['text']=="X" and btns[8]['text']=="X":
        s="X獲勝"
        x['text']=s
        win_flag=True
        for i in btns:
            i['state']='disable'
    elif btns[2]['text']=="X" and btns[4]['text']=="X" and btns[6]['text']=="X":
        s="X獲勝"
        x['text']=s
        win_flag=True
        for i in btns:
            i['state']='disable'
    elif btns[0]['text']=="X" and btns[3]['text']=="X" and btns[6]['text']=="X":
        s="X獲勝"
        x['text']=s
        win_flag=True
        for i in btns:
            i['state']='disable'
    elif btns[1]['text']=="X" and btns[4]['text']=="X" and btns[7]['text']=="X":
        s="X獲勝"
        x['text']=s
        win_flag=True
        for i in btns:
            i['state']='disable'
    elif btns[2]['text']=="X" and btns[5]['text']=="X" and btns[8]['text']=="X":
        s="X獲勝"
        x['text']=s
        win_flag=True
        for i in btns:
            i['state']='disable'

    for i in btns:
        if i['text']!="":
            c+=1

    if c==9:
        s="平手"
        x['text']=s
        for i in btns:
            i['state']='disable'

    game_data.append(f)
    player_flag=~player_flag



for i in range(0,3):
    for j in range(0,3):
        b=Button(root,width=15,height=3,command=lambda c=n:run(c))
        b.grid(row=i+1,column=j)
        btns.append(b)
        n+=1


root.mainloop()