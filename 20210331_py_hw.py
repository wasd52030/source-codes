from tkinter import *
import tkinter.font
import tkinter.messagebox

root=Tk()
root.resizable(0,0)
status_text=['現在是X','現在是O']
player=1
status=-1
level=3
btns=[]
grid_btn=[]
n=0

x=Label(root,text='由O開始',font=tkinter.font.Font(family="Arial", size=15))
x.grid(row=0)

#返回1 => 有人勝出
#返回0 => 平手
#返回-1 => 遊戲仍在進行
def judgment():
    global grid_btn,level
    row,column,lfcross,ricross,total=[],[],[],[],[]
    rowok,columnok,lfcrossok,ricrossok=False,False,False,False
    for i in range(len(grid_btn)):
        jd1,jd2=[],[]
        for j in range(len(grid_btn)):
            jd1.append(grid_btn[i][j]['text'])
            jd2.append(grid_btn[j][i]['text'])
            total.append(grid_btn[i][j]['text'])
            if i==j:
                lfcross.append(grid_btn[i][j]['text'])
            if i+j==len(grid_btn)-1:
                ricross.append(grid_btn[i][j]['text'])
        row.append(jd1)
        column.append(jd2)

    #set(list) => 獲得一去重之集合
    #也就是說，只要對上述集合求長度，如果為1即為全等
    for i in range(len(row)):
        for k in row[i]:
            if k!='':
                if len(set(row[i]))==1:
                    rowok=True
    
    for i in range(len(column)):
        for k in column[i]:
            if k!='':
                if len(set(column[i]))==1:
                    columnok=True

    for k in lfcross:
        if k!='':
            if len(set(lfcross))==1:
                lfcrossok=True
    
    for k in ricross:
        if k!='':
            if len(set(ricross))==1:
                ricrossok=True

    for i in range(len(grid_btn)):
        for j in range(len(grid_btn)):
            if grid_btn[i][j]['text']=='':
                nowin=False
            else:
                nowin=True

    no_void_cnt=0
    for k in total:
        if k!='':
           no_void_cnt+=1

    if rowok==True or columnok==True or lfcrossok==True or ricrossok==True:
        return 1
    elif no_void_cnt == level**2:
        return 0
    else:
        return -1

def run(btnid):
    global player,status,btns,status_text

    mark=['O','X']
    
    if player%2==1:
        player=1
    else:
        player=2

    if btns[btnid]['text']!='':
        tkinter.messagebox.showwarning('title','此格已被使用')
        player -= 1
    else:
        btns[btnid]['text']=mark[player-1]
    
    x['text']=status_text[player-1]

    status = judgment()
    player += 1

    if status ==1:
        player-=1
        x['text']='{}獲勝'.format(mark[player-1])
        for i in btns:
            i['state']='disable'
    elif status ==0:
        x['text']='平手'
        for i in btns:
            i['state']='disable'

def reset_game():
    global btns,player,status,n,level
    btns.clear()
    grid_btn.clear()
    n=0
    player=1
    status=-1
    x['text']='由O開始'
    game_status=[i for i in range(0,level**2)]
    game_window_init(level)

def game_window_init(level):
    global n,btns,grid_btn
    row=0
    for i in range(0,level):
        k=[]
        for j in range(0,level):
            b=Button(root,width=10,height=5,relief='groove',command=lambda c=n:run(c))
            b.grid(row=i+1,column=j)
            btns.append(b)
            k.append(b)
            n+=1
        row=i+1
        grid_btn.append(k)
    func_btn(row)

def next_level():
    global level,btns,grid_btn
    level+=1
    grid_btn.clear()
    game_window_init(level)

def func_btn(row):
    global level
    column=row+1
    reset=Button(root,text='重設',width=21,height=5,relief='groove',command=reset_game)
    reset.grid(row=row+1,columnspan=row-1)
    btn_next=Button(root,text='下一關',width=10,height=5,relief='groove',command=next_level)
    btn_next.grid(row=row+1,column=row-1)

def main():
    global level
    game_window_init(level)
    root.mainloop()

main()