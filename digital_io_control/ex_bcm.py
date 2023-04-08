import RPi.GPIO as GPIO
import sys
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

try:
    while True:
        LEDon = GPIO.output(4, 0)
        time.sleep(1)
        LEDoff = GPIO.output(4, 1)
        time.sleep(1)
finally:
    GPIO.cleanup()