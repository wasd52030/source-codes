import random
from tkinter import *
import tkinter.font
from threading import Timer

root = Tk()
btns = []
ans = StringVar()
Ans = ''.join([chr(random.randint(97, 122)) for i in range(random.randint(2, 10))])
u, v = 0, 0
Score = 0
score = StringVar()
g = []
r = [i for i in range(10)]


def run():
    global g, u, v, r, btns
    t = Timer(1, run)
    t.start()
    if u < len(btns) and v == 0:
        if r != []:
            d = random.sample(r, 1)[0]
            r.remove(d)
            z = [0, d]
            g.insert(0, z)
            if u != 0:
                for i in range(len(g)-1):
                    g[i+1][0] += 1
            for i in range(len(g)):
                btns[g[i][0]][g[i][1]]['text'] = 'X'
                if len(g) != 0:
                    for i in range(len(g)):
                        btns[g[i-1][0]][g[i][1]]['text'] = ' '
            u += 1
            v = 1 if u == len(btns) else 0
    elif v == 1:
        if u == 0:
            t.cancel()
            c['text'] = 'GAMEOVER'
            ans.set('')
            textbox1['state'] = 'disabled'
        else:
            for i in range(len(g)-1):
                btns[g[i][0]][g[i][1]]['text'] = ' '
            u -= 1
            btns[g[u][0]][g[u][1]]['text'] = ''
            g = g[:u]
            for i in range(len(g)):
                g[i][0] += 1
            if len(g) != 0:
                for i in range(len(g)):
                    btns[g[i][0]][g[i][1]]['text'] = 'X'
    print(g)


def judgment(event):
    global ans, Ans, score, Score, btns, g, u, v, r
    if ans.get() == Ans:
        Ans = ''.join([chr(random.randint(97, 122)) for i in range(random.randint(1, 5))])
        c['text'] = Ans
        Score += 1
        score.set(f'Score={str(Score)}')
        btns[g[u-1][0]][g[u-1][1]]['text'] = ''
    ans.set('')


if __name__ == "__main__":
    for i in range(10):
        x = []
        for j in range(10):
            b = Button(root, width=5, height=2)
            b.grid(row=i, column=j)
            x.append(b)
        btns.append(x)

    c = Label(root, text='a', font=tkinter.font.Font(family="Arial", size=15))
    c.grid(row=10, column=0, columnspan=3)
    c['text'] = Ans
    textbox1 = Entry(root, textvariable=ans)
    textbox1.grid(row=10, column=3, columnspan=4)
    textbox1.focus()
    textbox1.bind('<Return>', judgment)
    sc = Label(root, textvariable=score, font=tkinter.font.Font(family="Arial", size=15))
    sc.grid(row=10, column=7, columnspan=3)
    score.set(f'Score={str(Score)}')
    run()
    root.mainloop()
