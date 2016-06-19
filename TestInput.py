
import sys
import os
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN)

while 1:
    time.sleep(0.5)
    if GPIO.input(8) == GPIO.HIGH:
        sys.stdout.write('H')
    else:
        sys.stdout.write('L')



        
        
