import datetime 
import sys
import os
import RPi.GPIO as GPIO
import time
ts = time.time()
n=0
GPIO.setmode(GPIO.BOARD)
GPIO.setup(21, GPIO.IN)

while 1:
    time.sleep(0.5)
    if GPIO.input(21) == GPIO.HIGH:
        sys.stdout.write('H')
        old=1
    else:
        sys.stdout.write('L')
        if old == 1:
            tn= time.time()
            dt=tn-ts
            ts=tn
            n=n+1
            print [dt, n, 3600/dt]
            old=0



        
        
