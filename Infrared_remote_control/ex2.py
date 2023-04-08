import time
import RPi.GPIO as GPIO
import json
import sys

GPIO.setmode(GPIO.BCM)

GPIO_IR = 14
GPIO.setup(GPIO_IR,GPIO.IN)

def getIRsingal(start = 0, stop = 0):
  IRsignal = []
  while True:
    start = time.time()
    duringDown = start-stop

    while GPIO.input(GPIO_IR) == 0:
      start = time.time()
  
    while GPIO.input(GPIO_IR) == 1:
      stop = time.time()
      duringUp = stop - start
      if duringUp > 0.1 and len(IRsignal) > 0:
        print("-----------------")
        return IRsignal[1:]
    
    info = "Up:%7.f" % (duringUp*100000) + ", Down:%7.F" %(duringDown*100000)
    print(info)

    IRsignal.append(duringUp)

def recorder():
  keys = {}
  while True:
    key_name = input('Please input Key ID:')
    if key_name == 'exit':
      break
  
    keys[key_name] = getIRsingal()       

  src = open("OUT_FILE", 'w')
  src.write(json.dumps(keys))
  src.close 
   
recorder()  
GPIO.cleanup()  