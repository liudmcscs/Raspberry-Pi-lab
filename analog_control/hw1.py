import spidev
from numpy import interp
from time import sleep
import RPi.GPIO as GPIO

spi = spidev.SpiDev()
spi.open(0 ,0)

GPIO.setmode(GPIO.BCM)

def analogInput(channel):
    spi.max_speed_hz = 1350000
    adc = spi.xfer2([1, (8+channel)<<4, 0])
    data = ((adc[1]&3) << 8) + adc[2]
    return data

while True:
    output1 = analogInput(0)
    output1 = interp(output1, [0, 1023], [0, 100])
    output2 = analogInput(7)
    output2 = interp(output2, [0, 1023], [0, 100])    
    print("output1: {}".format(output1))
    print("output2: {}".format(output2))
    
    sleep(0.1)