from tkinter import *

root=Tk()
root.resizable(0,0)
s="由O開始"
btns=[]
game_data=[]
player_flag=True
n=0

x=Label(root,text=s,borderwidth=1,relief="solid",width=49,height=3)
x.grid(row=0,columnspan=3)

def win(n):
    global s
    s="{}獲勝".format(n)
    x['text']=s
    for i in btns:
        i['state']='disable'

def judgment(g):
    if btns[0]['text'] == btns[1]['text'] == btns[2]['text']==g:
        win(btns[0]['text'])
    elif btns[3]['text'] == btns[4]['text'] == btns[5]['text']==g:
        win(btns[3]['text'])
    elif btns[6]['text'] == btns[7]['text'] == btns[8]['text']==g:
        win(btns[6]['text'])
    elif btns[0]['text'] == btns[4]['text'] == btns[8]['text']==g:
        win(btns[0]['text'])
    elif btns[2]['text'] == btns[4]['text'] == btns[6]['text']==g:
        win(btns[2]['text'])
    elif btns[0]['text'] == btns[3]['text'] == btns[6]['text']==g:
        win(btns[0]['text'])
    elif btns[1]['text'] == btns[4]['text'] == btns[7]['text']==g:
        win(btns[1]['text'])
    elif btns[2]['text'] == btns[5]['text'] == btns[8]['text']==g:
        win(btns[2]['text'])

def run(btnid):
    global player_flag,s
    fword=""
    c=0
    if player_flag==True:
        fword='O'
        s="現在是O"
        btns[btnid]['text']=fword
        x['text']=s
    else:
        fword='X'
        s="現在是O"
        btns[btnid]['text']=fword
        x['text']=s

    judgment("O")
    judgment("X")

    for i in btns:
        if i['text']!="":
            c+=1

    if c==9:
        s="平手"
        x['text']=s
        for i in btns:
            i['state']='disable'

    game_data.append(win)
    player_flag=~player_flag

def main():
    global n
    for i in range(0,3):
        for j in range(0,3):
            b=Button(root,width=15,height=3,command=lambda c=n:run(c))
            b.grid(row=i+1,column=j)
            btns.append(b)
            n+=1
    root.mainloop()

main()