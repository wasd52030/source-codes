import RPi.GPIO as GPIO
from utils import numMap


class RGBLED:
    def __init__(self, red: int, green: int, blue: int) -> None:
        GPIO.setup(red, GPIO.OUT)
        GPIO.output(red, 0)
        GPIO.setup(green, GPIO.OUT)
        GPIO.output(green, 0)
        GPIO.setup(blue, GPIO.OUT)
        GPIO.output(blue, 0)

        self.r = GPIO.PWM(red, 2000)
        self.g = GPIO.PWM(green, 1999)
        self.b = GPIO.PWM(blue, 5000)
        self.r.start(100)
        self.g.start(100)
        self.b.start(100)

    def setColor(self, hexColor: int):
        red = (hexColor & 0xFF0000) >> 16
        green = (hexColor & 0x00FF00) >> 8
        blue = hexColor & 0x0000FF

        red = numMap(red, 0, 255, 0, 100)
        green = numMap(green, 0, 255, 0, 100)
        blue = numMap(blue, 0, 255, 0, 100)

        self.r.ChangeDutyCycle(red)
        self.g.ChangeDutyCycle(green)
        self.b.ChangeDutyCycle(blue)
