import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.IN)

try:
    while True:
        value01 = GPIO.input(17)
        print(value01)
        GPIO.output(4,value01)
finally:
    GPIO.cleanup()