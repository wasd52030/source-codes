import RPi.GPIO as GPIO
from PIL import ImageFont
import subprocess
import threading
import time
from rgbLED import RGBLED
from buzzer import buzzer
from ili9341 import ili9341


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# RGBLED
led1 = RGBLED(red=36, green=38, blue=40)

# LM358光敏電阻
GPIO.setup(11, GPIO.IN)

# LM393麥克風模組
GPIO.setup(13, GPIO.IN)

# 蜂鳴器
buz1 = buzzer(15)

screen1 = ili9341(dc=18, reset=22, led=12)

font = ImageFont.truetype(
    "/usr/share/fonts/truetype/opentype/NotoSansCJK-Regular.ttc", 20
)


def lightTask():
    while 1:
        if GPIO.input(11):
            led1.setColor(0x00FF00)
            # tBuzz = threading.Thread(target=buzzTask, daemon=True)
            # tBuzz.start()
            # tBuzz.join()
        else:
            led1.setColor(0x000000)

        time.sleep(0.4)


def piSysInfo():
    global font

    # 把畫面清空
    screen1.draw.rectangle((0, 0, 340, 240), fill="#000000")

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

    screen1.draw.text((x, y), IP, font=font, fill="#FFFFFF")
    y += font.getsize(IP)[1]
    screen1.draw.text((x, y), CPU, font=font, fill="#FFFF00")
    y += font.getsize(CPU)[1]
    screen1.draw.text((x, y), MemUsage, font=font, fill="#00FF00")
    y += font.getsize(MemUsage)[1]
    screen1.draw.text((x, y), Disk, font=font, fill="#0000FF")
    y += font.getsize(Disk)[1]
    screen1.draw.text((x, y), Temp, font=font, fill="#FF00FF")

    screen1.drawImg16BitColor()


def buzzTask():
    buz1.beep(5)


def mainTask():
    while 1:
        print(GPIO.input(13))
        piSysInfo()
        time.sleep(1)


def main():
    tMain = threading.Thread(target=mainTask, daemon=True)
    tLight = threading.Thread(target=lightTask, daemon=True)
    
    tMain.start()
    tLight.start()

    tLight.join()
    tMain.join()


if __name__ == "__main__":
    main()
