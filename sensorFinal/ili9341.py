import time
import RPi.GPIO as GPIO
import spidev  # 樹莓派与螢幕的通訊協議為SPI，參考: https://github.com/doceme/py-spidev
from PIL import Image, ImageFont, ImageDraw  # 利用PIL將圖片的像素寫到螢幕


class ili9341:
    def __init__(self, dc: int, reset: int, led: int) -> None:
        self.dc = dc
        self.rst = reset
        self.led = led
        self.spi = spidev.SpiDev()  # https://github.com/doceme/py-spidev
        self.spi.open(0, 0)
        self.spi.max_speed_hz = 24000000  # CLK MAX freq
        self.spi.mode = 0x00  # SPI的模式，9341为模式spi0
        self.width = 320
        self.height = 240
        self.image = Image.new("RGB", (self.width, self.height))
        self.draw = ImageDraw.Draw(self.image)

        GPIO.setup(self.dc, GPIO.OUT)
        GPIO.setup(self.rst, GPIO.OUT)
        GPIO.setup(self.led, GPIO.OUT)

        self.initialize()
        self.setWindow()

    def reset(self):  # 重置時序
        GPIO.output(self.rst, 1)
        time.sleep(0.050)
        GPIO.output(self.rst, 0)
        time.sleep(0.050)
        GPIO.output(self.rst, 1)
        time.sleep(0.050)

    def sendCommand(self, command, *bytes):  # 發送指令(DC為LOW)和數據(DC為HIGH)
        GPIO.output(self.dc, 0)
        self.spi.writebytes([command])
        if len(bytes) > 0:
            GPIO.output(self.dc, 1)
            self.spi.writebytes(list(bytes))

    def sendManyBytes(self, bytes):  # 發送螢幕數據
        GPIO.output(self.dc, 1)
        self.spi.writebytes(bytes)

    def initialize(self):  # 屏幕初始化
        GPIO.output(self.led, 1)  # LED.high();
        self.reset()
        self.sendCommand(0xCF, 0x00, 0xC1, 0x30)
        self.sendCommand(0xEF, 0x03, 0x80, 0x02)
        self.sendCommand(0xED, 0x64, 0x03, 0x12, 0x81)
        self.sendCommand(0xE8, 0x85, 0x00, 0x78)
        self.sendCommand(0xCB, 0x39, 0x2C, 0x00, 0x34, 0x02)
        self.sendCommand(0xF7, 0x20)
        self.sendCommand(0xEA, 0x00, 0x00)
        self.sendCommand(0xC0, 0x23)  # Power control --VRH[5:0]
        self.sendCommand(0xC1, 0x10)  # Power control # SAP[2:0];BT[3:0]
        self.sendCommand(0xC5, 0x3E, 0x28)  # VCM control
        self.sendCommand(0xC7, 0x86)  # VCM control2
        self.sendCommand(0x36, 0x48)  #  Memory Access Control
        self.sendCommand(0x3A, 0x55)
        self.sendCommand(0xB1, 0x00, 0x18)
        self.sendCommand(0xB6, 0x08, 0x82, 0x27)  #  Display Function Control
        self.sendCommand(0xF2, 0x00)  #  3Gamma Function Disable
        self.sendCommand(0x26, 0x01)  # Gamma curve selected

        # Set Gamma
        self.sendCommand(
            0xE0,
            0x0F,
            0x31,
            0x2B,
            0x0C,
            0x0E,
            0x08,
            0x4E,
            0xF1,
            0x37,
            0x07,
            0x10,
            0x03,
            0x0E,
            0x09,
            0x00,
        )

        # Set Gamma
        self.sendCommand(
            0xE1,
            0x00,
            0x0E,
            0x14,
            0x03,
            0x11,
            0x07,
            0x31,
            0xC1,
            0x48,
            0x08,
            0x0F,
            0x0C,
            0x31,
            0x36,
            0x0F,
        )

        self.sendCommand(0x11)  # Exit Sleep
        self.sendCommand(0x29)  # Display on

    def setWindow(self):
        self.sendCommand(0x2A)
        # Column addr set
        x0 = 0
        bytes = []
        bytes.append(x0 >> 8)
        bytes.append(x0)
        self.sendManyBytes(bytes)
        # XSTART
        x1 = self.width - 1
        bytes = []
        bytes.append(x1 >> 8)
        bytes.append(x1)
        self.sendManyBytes(bytes)
        # XEND
        self.sendCommand(0x2B)
        # Row addr set
        bytes = []
        bytes.append(0 >> 8)
        bytes.append(0)
        self.sendManyBytes(bytes)
        # YSTART
        y1 = self.width - 1
        bytes = []
        bytes.append(y1 >> 8)
        bytes.append(y1)
        self.sendManyBytes(bytes)
        # YEND
        self.sendCommand(0x2C)
        print("setWindow done")

    def drawImg16BitColor(self):
        bytes = []
        i = 0
        GPIO.output(self.dc, 1)
        for x in range(0, self.width):
            for y in range(self.height - 1, -1, -1):
                colorValue = self.image.getpixel((x, y))
                red = colorValue[0]
                green = colorValue[1]
                blue = colorValue[2]
                red = red >> 3  # st7735s的紅色占5位
                green = green >> 2  # st7735s的綠色占6位
                blue = blue >> 3  # st7735s的藍色占5位
                highBit = 0 | (red << 3) | (green >> 3)
                lowBit = 0 | (green << 5) | blue
                bytes.append(highBit)
                bytes.append(lowBit)

        # self.width*self.height*2 每个像素寫入2个byte。
        # 以下for lopp是用來控制每次傳入的陣列長度，以避免這個Error：OverflowError: Argument list size exceeds 4096 bytes.
        for j in range(2000, self.width * self.height * 2, 2000):
            self.sendManyBytes(bytes[i:j])
            i = i + 2000
        self.sendManyBytes(bytes[i : self.width * self.height * 2])
