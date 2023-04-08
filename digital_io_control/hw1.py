import RPi.GPIO as GPIO
import sys
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN)
GPIO.setup(6,GPIO.IN)
GPIO.setup(4,GPIO.IN)
GPIO.setup(26,GPIO.OUT)
try:
    button1=0
    button2=3
    button3=0
    state=0
    GPIO.output(26,0)
    while True:
        button1 = GPIO.input(17)
        button2 = GPIO.input(6)
        button3 = GPIO.input(4)
        print("button2: "button2)
        if button1 == 1 and state == 3:
            state = 1
        elif button2 == 1 and state == 1:
            state = 2
        elif button2 == 0 and state == 2:
            state = 1
            print("here")
        if button3 == 1:
            state = 3
            GPIO.output(26,0)
        if state == 1:
            GPIO.output(26,1)
            time.sleep(1)
            GPIO.output(26,0)
            time.sleep(1)   
        elif state == 2:
            GPIO.output(26,1)
finally:
        GPIO.cleanup()
