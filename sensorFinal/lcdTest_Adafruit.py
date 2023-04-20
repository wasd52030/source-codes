#!/usr/bin/python3

import time
from datetime import datetime
import threading

from PIL import Image, ImageDraw, ImageFont

from adafruit_blinka.microcontroller.bcm283x.pin import Pin
import digitalio
import board
from adafruit_rgb_display import ili9341
import adafruit_dht


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
            time.sleep(2.0)
        except Exception as error:
            device.exit()
            raise error
        time.sleep(2)


def envMonitor():
    global font, draw, image, disp,dht11_data

    # 把畫面清空
    draw.rectangle((0, 0, 340, 240), fill="#000000")

    currTime = datetime.now()
    timeText = f"現在時間：{currTime.hour}：{currTime.minute}：{currTime.second}"
    print(timeText)

    x, y = 0, -2
    draw.text((x, y), timeText, font=font, fill="#FFFFFF")
    y += font.getsize(timeText)[1]
    
    temp_dht11=[0,0]
    if len(dht11_data)>0:
        temp_dht11=dht11_data

    temp = f"現在溫度：{temp_dht11[0]}°C"
    draw.text((x, y), temp, font=font, fill="#FFFFFF")
    y += font.getsize(temp)[1]
    
    humi=f"現在濕度：{temp_dht11[1]}%"
    draw.text((x, y), humi, font=font, fill="#FFFFFF")
    y += font.getsize(humi)[1]
    

    disp.image(image)

def mainTask():
    while 1:
        envMonitor()
        time.sleep(0.5)


# Configuration for CS and DC pins (these are PiTFT defaults):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D24)
reset_pin = digitalio.DigitalInOut(board.D25)

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 24000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()
disp = ili9341.ILI9341(
    spi,
    rotation=270,  # 2.2", 2.4", 2.8", 3.2" ILI9341
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
)

image = Image.new("RGB", (320, 240))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype(
    "/usr/share/fonts/truetype/opentype/NotoSansCJK-Regular.ttc", 20
)

dht11_data = []

tDht11 = threading.Thread(target=getDTH11Data, daemon=True)

tMain = threading.Thread(target=mainTask, daemon=True)

tMain.start()
tDht11.start()
tDht11.join()
tMain.join()
