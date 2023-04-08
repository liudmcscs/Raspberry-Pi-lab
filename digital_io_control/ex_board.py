import RPi.GPIO as GPIO
import sys
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

try:
    while True:
        LEDon = GPIO.output(7, 0)
        time.sleep(1)
        LEDoff = GPIO.output(7, 1)
        time.sleep(1)
finally:
        GPIO.cleanup()