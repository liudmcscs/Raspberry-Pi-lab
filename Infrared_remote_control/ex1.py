import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)

GPIO_IR = 14
GPIO.setup(GPIO_IR,GPIO.IN)

start = 0
stop = 0

while True:
  start = time.time()
  duringDown = start-stop

  while GPIO.input(GPIO_IR) == 0:
    start = time.time()
  while GPIO.input(GPIO_IR) == 1:
    stop = time.time()
    duringUp = stop - start
  if duringUp > 0.1:
    print("-----------------")
  info = "Up:%7.f" % (duringUp*100000) + ", Down:%7.F" %(duringDown*100000)
  print (info)



GPIO.cleanup()  