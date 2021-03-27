from tkinter import *
import tkinter.font
import tkinter.messagebox
import sys

root=Tk()
root.resizable(0,0)
status_text=['現在是X','現在是O']
player=1
status=-1
btns=[]
game_status=[i for i in range(0,9)]
n=0

x=Label(root,text='由O開始',font=tkinter.font.Font(family="Arial", size=16))
x.grid(row=0,columnspan=3)

#返回1 => 有人勝出
#返回0 => 平手
#返回-1 => 遊戲仍在進行
def judgment():
    global game_status

    if game_status[0] == game_status[1]  == game_status[2] :
        return 1
    elif game_status[3] == game_status[4]  == game_status[5]:
        return 1
    elif game_status[6] == game_status[7]  == game_status[8]:
        return 1
    elif game_status[0] == game_status[4]  == game_status[8]:
        return 1
    elif game_status[2] == game_status[4]  == game_status[6]:
        return 1
    elif game_status[0] == game_status[3]  == game_status[6]:
        return 1
    elif game_status[1] == game_status[4]  == game_status[7]:
        return 1
    elif game_status[2] == game_status[5]  == game_status[8]:
        return 1
    elif (game_status[0] != 0 and game_status[1] != 1 and game_status[2] != 2 and 
          game_status[3] != 3 and game_status[4] != 4 and game_status[5] != 5 and 
          game_status[6] != 6 and game_status[7] != 7 and game_status[8] != 8):
        return 0
    else:
        return -1

def run(btnid):
    global player,status,game_status,btns
    
    if player%2==1:
        player=1
    else:
        player=2
    
    if player==1:
        mark='O'
        x['text']=status_text[player-1]
    else:
        mark='X'
        x['text']=status_text[player-1]
    
    if btnid == 0 and game_status[0] == 0:
        game_status[0] = mark
    elif btnid == 1 and game_status[1] == 1:
        game_status[1] = mark
    elif btnid == 2 and game_status[2] == 2:
        game_status[2] = mark
    elif btnid == 3 and game_status[3] == 3:
        game_status[3] = mark
    elif btnid == 4 and game_status[4] == 4:
        game_status[4] = mark
    elif btnid == 5 and game_status[5] == 5:
        game_status[5] = mark
    elif btnid == 6 and game_status[6] == 6:
        game_status[6] = mark
    elif btnid == 7 and game_status[7] == 7:
         game_status[7] = mark
    elif btnid == 8 and game_status[8] == 8:
        game_status[8] = mark
    else:
        tkinter.messagebox.showwarning('title','此格已被使用')
        player -= 1
        x['text']=status_text[player-1]
                
    status = judgment()
    player += 1

    btns[btnid]['text']=game_status[btnid]
    if status ==1:
        x['text']='{}獲勝'.format(mark)
        for i in btns:
            i['state']='disable'
    elif status ==0:
        x['text']='平手'
        for i in btns:
            i['state']='disable'

def menu_init():
    MainMenu = tkinter.Menu(root)   #創建主要選單欄
    root.config(menu=MainMenu)  #綁定主要選單
    menu1 = tkinter.Menu(MainMenu,tearoff=0)  #創建子選單欄綁在父容器下
    menu1.add_command(label='重開一局',command=reset_game)  #新增子選單1內的項目一
    menu1.add_command(label='結束',command=lambda:sys.exit(0))  #新增子選單1內的項目二
    MainMenu.add_cascade(label='選項', menu=menu1)  #命名父選單第一欄的名稱, 並綁定子選單1所有項目

def reset_game():
    global btns,player,status,game_status,n
    btns.clear()
    n=0
    player=1
    status=-1
    x['text']='由O開始'
    game_status=[i for i in range(0,9)]
    game_window_init()

def game_window_init():
    global n
    for i in range(0,3):
        for j in range(0,3):
            b=Button(root,width=10,height=5,relief='groove',command=lambda c=n:run(c))
            b.grid(row=i+1,column=j)
            btns.append(b)
            n+=1

def main():
    game_window_init()
    menu_init()
    root.mainloop()

main()