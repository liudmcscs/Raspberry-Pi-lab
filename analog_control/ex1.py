import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)

p1=GPIO.PWM(4,1000)
p2=GPIO.PWM(17,50)

p1.start(0)
p2.start(50)

while True:
    for dc in range(5,101,5):
        p1.ChangeDutyCycle(dc)
        p2.ChangeFrequency(dc)
        time.sleep(0.2)


