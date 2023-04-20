import digitalio
import board
from PIL import Image, ImageDraw
from adafruit_rgb_display import ili9341
from adafruit_blinka.microcontroller.bcm283x.pin import Pin


class ili9341_Adafruit:
    def __init__(self, cs:Pin, dc:Pin, rst:Pin) -> None:
        self.buadrate = 24000000
        self.spi = board.SPI()
        self.disp = ili9341.ILI9341(
            self.spi,
            rotation=270,  # 2.2", 2.4", 2.8", 3.2" ILI9341
            dc=digitalio.DigitalInOut(dc),
            cs=digitalio.DigitalInOut(cs),
            rst=digitalio.DigitalInOut(rst),
            baudrate=self.buadrate,
        )
        self.image = Image.new("RGB", (320, 240))
        self.draw = ImageDraw.Draw(self.image)
