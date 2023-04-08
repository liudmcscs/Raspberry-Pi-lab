import time
import RPi.GPIO as GPIO
import json
import sys
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO_IR = 14
GPIO.setup(GPIO_IR,GPIO.IN)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)

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

    IRsignal.append(duringUp)
  print ("Got IRsignal")
 
def compair(s1, s2, rang):
  leng = min(len(s1), len(s2))

  for i in range(leng):
    if abs(s1[i] - s2[i]) >rang:
      return False
  return True

def decode(s, signalrec, rang):
  for name in signalrec.keys():
    if compair(s, signalrec[name], rang):
      return name
  return None 

   
src = open("OUT_FILE", 'r')
signals =json.loads(src.read())
src.close

p1=GPIO.PWM(4,50)
p2=GPIO.PWM(17,50)

p1.start(50)
p2.start(50)

while True:
  IRsignals = getIRsingal()
  reminput = decode(IRsignals, signals, 0.001) 
  if reminput == '1':
    p1.ChangeDutyCycle(50)
    p1.ChangeFrequency(1)
    p2.ChangeDutyCycle(0)
    print(reminput)
  elif reminput == '2':
    p1.ChangeDutyCycle(50)
    p1.ChangeFrequency(1000)
    print(reminput)
  elif reminput == '3':
    p2.ChangeDutyCycle(50)
    p1.ChangeDutyCycle(0)
    p2.ChangeFrequency(0.5)
    print(reminput)
  elif reminput == '4':
    p1.ChangeDutyCycle(50)
    p2.ChangeDutyCycle(50)
    p1.ChangeFrequency(1)
    p2.ChangeFrequency(1)
    print(reminput)
GPIO.cleanup()  