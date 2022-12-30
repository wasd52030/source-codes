import random
import os

data = []
money = 100
wincounter = 0
user_input = []
kin_flag = 0
rein = 0


def game_input():
    global user_input, money, rein, wincounter, data
    user_input.clear()
    if rein != 1:
        money -= 10
    rein = 0
    print("你有%d塊" % money)
    print("輸入一四位數的數字(不得重複):", end="")
    user_input = list(map(int, input()))
    if len(set(user_input)) != len(user_input):
        print("輸入的數字有重複，請重新輸入")
        rein = 1
        game_input()
    rein = 0
    wincounter += 1
    print("題目 : ", end="")
    print(data)
    print(user_input)
    run_game()


def calc():
    global wincounter, money
    if wincounter <= 5:
        money += 10
        money += 5
    elif wincounter > 5:
        money -= 5


def run_game():
    global data, user_input, money, wincounter, rein

    rein = 0
    allclear, only_value = 0, 0

    u = ([item, index] for index, item in enumerate(data))
    v = ([item, index] for index, item in enumerate(user_input))
    for du, dv in zip(u, v):
        if dv[0] in data:
            if dv[0] == du[0] and dv[1] == du[1]:
                allclear += 1
            else:
                only_value += 1

    print("皆對%d個，位置錯%d個,猜了%d次" % (allclear, only_value, wincounter))
    if allclear == 4:
        print("win")
        calc()
        main()
    else:
        game_input()
        rein = 0


def main():
    global data

    print("現有金額 : %d" % money)
    print("輸入1進遊戲，輸入0離開:", end="")
    kin_flag = int(input())
    if kin_flag == 1:
        data = random.sample(list(range(0, 10)), 4)
        print(data)
        game_input()
    elif kin_flag==0:
        os._exit(0)
    else:
        print("不支援指令")
        main()


main()
