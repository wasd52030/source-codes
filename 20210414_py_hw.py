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
num=random.randint(5,15)
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
    for n in btns:
        n['text']=''
    for i in range(num):
        btns[random.randint(0,99)]['text']='X'

def set_time_and_rand():
    global timeText,cnt,num,tmain,level,score
    cnt+=1
    timeText.set(f'{cnt}秒')
    LevelText.set(f'現在是第{level}關，共{score}分')
    ScoreText.set(f'共有{str(num)}隻地鼠')
    t1=Timer(1,set_time_and_rand)
    t1.start()
    if cnt==15:
        for a in btns: a['state']='disable'
        tmain.cancel()
        t1.cancel()
        tkinter.messagebox.showwarning('','遊戲結束')
        return
    elif cnt%5==0:
        num=random.randint(5,15)
        level+=1
        bnttext_set()
    

tmain=Timer(1,function=set_time_and_rand)


timeText.set(f'{cnt}秒')
ScoreText.set(f'共有{str(num)}隻地鼠')
LevelText.set(f'現在是第{level}關，共{score}分')

fontsize=tkinter.font.Font(family="Arial", size=13)
Label(root,textvariable=LevelText,font=fontsize).grid(row=0,columnspan=10)
Label(root,textvariable=timeText,font=fontsize).grid(row=1,columnspan=10)
Label(root,textvariable=ScoreText,font=fontsize).grid(row=2,columnspan=10)

def game_init():
    global btns
    bid=0
    for i in range(0,10):
        for j in range(0,10):
            b=Button(root,height=2,width=4,command=lambda id=bid:judgment(id))
            b.grid(row=i+4,column=j)
            btns.append(b)
            bid+=1
    bnttext_set()

def main():
    game_init()
    tmain.start()
    root.mainloop()

main()