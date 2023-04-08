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
while True:
  IRsignals = getIRsingal()
  print("press %s" % ( decode(IRsignals, signals, 0.001) ))

GPIO.cleanup()  