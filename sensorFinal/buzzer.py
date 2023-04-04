import RPi.GPIO as GPIO
import asyncio
import time


class buzzer:
    def __init__(self, pin: int) -> None:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 1)

        self.buzz = GPIO.PWM(pin, 10)
        self.buzz.start(0)

    def beep(self, x: int):
        k = False
        for _ in range(x):
            if not k:
                self.buzz.ChangeFrequency(440)
            else:
                self.buzz.ChangeFrequency(330)
                self.buzz.ChangeDutyCycle(50)
            k = not k
            time.sleep(0.5)
            self.buzz.ChangeDutyCycle(0)
            # await asyncio.sleep(0.5)
