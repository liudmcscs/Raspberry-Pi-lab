import time
import sys
import Adafruit_DHT #BCM PIN
GPIO_PIN = 4

print('press control+C to stop the program')
  
while True:
  h, t = Adafruit_DHT.read_retry(11, 4)  
  print('temperature={0:0.1f} C humidity={1:0.1f}%'.format(t, h))     
