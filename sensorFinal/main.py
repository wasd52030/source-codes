#!/usr/bin/python3

import RPi.GPIO as GPIO
from PIL import ImageFont
import subprocess
import threading
import time
from ili9341_Adafruit import ili9341_Adafruit
from adafruit_blinka.microcontroller.bcm283x.pin import Pin
import adafruit_dht
from rgbLED import RGBLED
from buzzer import buzzer
from datetime import datetime
import requests


def getDTH11Data():
    global dht11_data

    device = adafruit_dht.DHT11(Pin(26))
    while 1:
        try:
            dht11_data = [device.temperature, device.humidity]
            print(f"dht11_data={dht11_data}")
        except RuntimeError as error:
            # Errors happen fairly often, DHT's are hard to read, just keep going
            print(error.args[0])
            time.sleep(2)
        except Exception as error:
            device.exit()
            raise error
        time.sleep(5)


def tempNotify():
    global dht11_data, headers

    temp_dht11 = [0, 0]
    while 1:
        if len(dht11_data) > 0:
            temp_dht11 = dht11_data

        if temp_dht11[0] != 0 and temp_dht11[1] != 0:
            requests.post(
                f"https://notify-api.line.me/api/notify?message=現在溫度：{temp_dht11[0]}°C",
                headers=headers,
            )
            requests.post(
                f"https://notify-api.line.me/api/notify?message=現在濕度：{temp_dht11[1]}%",
                headers=headers,
            )
        elif temp_dht11[0] != 0:
            requests.post(
                f"https://notify-api.line.me/api/notify?message=現在溫度：{temp_dht11[0]}°C",
                headers=headers,
            )
        elif temp_dht11[1] != 0:
            requests.post(
                f"https://notify-api.line.me/api/notify?message=現在濕度：{temp_dht11[1]}%",
                headers=headers,
            )
        time.sleep(60)


def lightTask():
    global light, warning
    while 1:
        if GPIO.input(17) or warning:
            light = False
        else:
            light = True
        time.sleep(0.5)


def micTask():
    global mic, warning
    while 1:
        if GPIO.input(27) or warning:
            mic = False
        else:
            mic = True
        time.sleep(0.5)


def piSysInfo():
    global font

    # 把畫面清空
    screen.draw.rectangle((0, 0, 340, 240), fill="#000000")

    cmd = "hostname -I | cut -d' ' -f1"
    IP = "IP: " + subprocess.check_output(cmd, shell=True).decode("utf-8")
    cmd = "top -bn1 | grep load | awk '{printf \"CPU負載: %.2f%%\", $(NF-2)}'"
    CPU = subprocess.check_output(cmd, shell=True).decode("utf-8")
    cmd = "free -m | awk 'NR==2{printf \"記憶體: %s/%s MB  %.2f%%\", $3,$2,$3*100/$2 }'"
    MemUsage = subprocess.check_output(cmd, shell=True).decode("utf-8")
    cmd = 'df -h | awk \'$NF=="/"{printf "硬碟: %d/%d GB  %s", $3,$2,$5}\''
    Disk = subprocess.check_output(cmd, shell=True).decode("utf-8")
    cmd = "cat /sys/class/thermal/thermal_zone0/temp |  awk '{printf \"CPU溫度: %.1f C\", $(NF-0) / 1000}'"
    Temp = subprocess.check_output(cmd, shell=True).decode("utf-8")

    x, y = 0, -2

    screen.draw.text((x, y), IP, font=font, fill="#FFFFFF")
    y += font.getsize(IP)[1]
    screen.draw.text((x, y), CPU, font=font, fill="#FFFF00")
    y += font.getsize(CPU)[1]
    screen.draw.text((x, y), MemUsage, font=font, fill="#00FF00")
    y += font.getsize(MemUsage)[1]
    screen.draw.text((x, y), Disk, font=font, fill="#0000FF")
    y += font.getsize(Disk)[1]
    screen.draw.text((x, y), Temp, font=font, fill="#FF00FF")

    screen.disp.image(screen.image)


def envMonitor():
    global font, mic, light, warning
    
    # print(light, mic)

    # 把畫面清空
    screen.draw.rectangle((0, 0, 340, 240), fill="#000000")

    currTime = datetime.now()
    timeText = f"現在時間: {currTime.hour:>02}：{currTime.minute:>02}：{currTime.second:>02}"

    # print(timeText,light)
    lightStatus = "亮度正常" if light or warning else "請開燈！"
    micStatus = "音量正常" if mic or warning else "請小聲！"

    x, y = 0, -2
    screen.draw.text((x, y), timeText, font=font, fill="#FFFFFF")
    y += font.getsize(timeText)[1]
    screen.draw.text(
        xy=(x, y),
        text=lightStatus,
        font=font,
        fill="#FFFFFF" if light or warning else "#FF0000",
    )
    y += font.getsize(lightStatus)[1]
    screen.draw.text(
        xy=(x, y),
        text=micStatus,
        font=font,
        fill="#FFFFFF" if mic or warning else "#FF0000",
    )
    y += font.getsize(micStatus)[1]

    temp_dht11 = [0, 0]
    if len(dht11_data) > 0:
        temp_dht11 = dht11_data

        temp = f"現在溫度：{temp_dht11[0]}°C"
        screen.draw.text((x, y), temp, font=font, fill="#FFFFFF")
        y += font.getsize(temp)[1]

        humi = f"現在濕度：{temp_dht11[1]}%"
        screen.draw.text((x, y), humi, font=font, fill="#FFFFFF")
        y += font.getsize(humi)[1]
    else:
        text = "正在讀取溫溼度資訊"
        screen.draw.text((x, y), text, font=font, fill="#FFFFFF")
        y += font.getsize(text)[1]

    screen.disp.image(screen.image)


def warningTask():
    led1.setColor(0xFF0000)
    buz1.beep(5)


def mainTask():
    global mic, light, warning, headers

    while 1:
        if (not light) and (not mic):
            # print(warning)
            warning = True
            tBuzz = threading.Thread(target=warningTask, daemon=True)
            tBuzz.start()
            tBuzz.join()
            warning = False
            # print(warning)

        elif not light:
            led1.setColor(0x00FF00)
            requests.post(
                f"https://notify-api.line.me/api/notify?message=太暗了，請開燈！",
                headers=headers,
            )
        elif not mic:
            led1.setColor(0x0000FF)
            requests.post(
                f"https://notify-api.line.me/api/notify?message=太吵了，請小聲！",
                headers=headers,
            )
        else:
            led1.setColor(0x000000)
        envMonitor()


def main():
    tMain = threading.Thread(target=mainTask, daemon=True)
    tLight = threading.Thread(target=lightTask, daemon=True)
    tMic = threading.Thread(target=micTask, daemon=True)
    tDht11 = threading.Thread(target=getDTH11Data, daemon=True)
    tTempNotify = threading.Thread(target=tempNotify, daemon=False)

    tMain.start()
    tLight.start()
    tMic.start()
    tDht11.start()
    tTempNotify.start()

    tMain.join()
    tLight.join()
    tMic.join()
    tDht11.join()
    tTempNotify.join()


if __name__ == "__main__":
    GPIO.setwarnings(False)
    # 為架接Adafruit的ili9341驅動，把編碼改成BCM模式
    GPIO.setmode(GPIO.BCM)

    # RGBLED
    led1 = RGBLED(red=16, green=20, blue=21)

    # LM358光敏電阻
    GPIO.setup(17, GPIO.IN)

    # LM393麥克風模組
    GPIO.setup(27, GPIO.IN)

    # 蜂鳴器
    buz1 = buzzer(22)

    # 光敏電阻狀態
    light = True

    # 壓電麥克風狀態
    mic = True

    # 警報狀態
    warning = False

    # 溫溼度資料
    dht11_data = []

    # line notify header
    headers = {"Authorization": "Bearer 114514"}

    screen = ili9341_Adafruit(cs=Pin(8), dc=Pin(24), rst=Pin(25))

    font = ImageFont.truetype(
        "/usr/share/fonts/truetype/opentype/NotoSansCJK-Regular.ttc", 20
    )

    main()
