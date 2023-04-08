import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
p1=GPIO.PWM(4,1000)
p1.start(50)
while True:
    print('choose items for setting: ')
    print('1.frequency')
    print('2.luminance')
    item = input()
    if item == 1: 
      print('input your frequency: ')
      frequency = input()
      p1.ChangeFrequency(frequency)
    elif item == 2:  
      print('input your luminance: ')
      luminance = input()
      p1.ChangeDutyCycle(luminance)


