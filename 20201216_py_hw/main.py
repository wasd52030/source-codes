import random
data = []
money = 100
yeslocate = False
yesvalue = False
justyesvalue = 0
wincounter = 0
doubleyes = 0
user_input = []
kin_flag = 0
rein = 0


def game_input():
    global user_input, money, doubleyes, justyesvalue, rein, wincounter, data
    user_input.clear()
    if rein != 1:
        money -= 10
    rein = 0
    doubleyes = 0
    justyesvalue = 0
    print("你有%d塊" % money)
    print("輸入一四位數的數字(不得重複):", end="")
    a = input()
    for k in range(0, len(a)):
        user_input.append(int(a[k]))
    for a in range(0, len(user_input)-1):
        if user_input[a] == user_input[a+1]:
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
    global data, user_input, money, yesvalue, yeslocate, doubleyes, justyesvalue, wincounter, rein
    rein = 0
    for i in range(0, len(user_input)):
        for x in data:
            if user_input[i] == x:
                yesvalue = True
                break
            else:
                yesvalue = False

        if user_input[i] == data[i]:
            yeslocate = True
        else:
            yeslocate = False

        if yeslocate == True and yeslocate == True:
            doubleyes += 1
        if yeslocate != True and yesvalue == True:
            justyesvalue += 1

    print("皆對%d個，位置錯%d個,猜了%d次" % (doubleyes, justyesvalue, wincounter))
    if doubleyes == 4:
        print("win")
        calc()
        main()
    else:
        game_input()
        rein = 0


def main():
    global data
    while True:
        print("現有金額 : %d" % money)
        print("輸入1進遊戲，輸入0離開:", end="")
        kin_flag = int(input())
        if kin_flag == 1:
            data = random.sample(list(range(0,10)), 4)
            print(data)
            game_input()
        elif kin_flag == 0:
            break


main()
