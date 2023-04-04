import time
from datetime import datetime
import digitalio
import board
import subprocess
from PIL import Image, ImageDraw,ImageFont
from adafruit_rgb_display import ili9341

def envMonitor():
    global font,draw,image

    # 把畫面清空
    draw.rectangle((0, 0, 340, 240), fill="#000000")

    currTime = datetime.now()
    timeText = f"現在時間：{currTime.hour}：{currTime.minute}：{currTime.second}"

    # lightStatus = "亮度正常" if light else "請開燈！"

    x, y = 0, -2
    draw.text((x, y), timeText, font=font, fill="#FFFFFF")
    y += font.getsize(timeText)[1]
    disp.image(image)


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

while 1:
    envMonitor()