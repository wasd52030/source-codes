from threading import Timer
from tkinter import *
import tkinter.messagebox
import random
import tkinter.font

root=Tk()
btns=[]
cnt=0
score=0
level=1
num=0
timeText=StringVar()
ScoreText=StringVar()
LevelText=StringVar()

def judgment(bid):
    global score,level
    if btns[bid]['text']!='':
            btns[bid]['text']=''
            score+=1

def bnttext_set():
    global num
    num=random.randint(5,15)
    temp=[]
    for i in btns: i['text']=''
    for i in range(num):
        temp.append(random.randint(0,99))
        j=0
        while j<i:
            if temp[i]==temp[j]:
                temp[i]=random.randint(0,99)
                j=0
            else:
                j+=1
    for i in temp: btns[i]['text']='X'
        

def run_game():
    global timeText,cnt,num,level,score
    timeText.set(f'{cnt}秒')
    LevelText.set(f'現在是第{level}關，共{score}分')
    ScoreText.set(f'共有{str(num)}隻地鼠')
    t1=Timer(1,run_game)
    t1.start()
    cnt+=1
    if cnt==15:
        for a in btns: a['state']='disable'
        t1.cancel()
        tkinter.messagebox.showwarning('','遊戲結束')
        return
    elif cnt%5==0:
        level+=1
        bnttext_set()

fontsize=tkinter.font.Font(family="Arial", size=13)
Label(root,textvariable=LevelText,font=fontsize).grid(row=0,columnspan=10)
Label(root,textvariable=timeText,font=fontsize).grid(row=1,columnspan=10)
Label(root,textvariable=ScoreText,font=fontsize).grid(row=2,columnspan=10)

def game_init():
    global btns,num
    bid=0
    for i in range(0,10):
        for j in range(0,10):
            b=Button(root,height=2,width=4,relief='groove',command=lambda id=bid:judgment(id))
            b.grid(row=i+4,column=j)
            btns.append(b)
            bid+=1
    bnttext_set()
    run_game()

def main():
    game_init()
    root.mainloop()

main()