
import sys
import os
import RPi.GPIO as GPIO
import time
i=0
OptoIn    = 21
Switch_K1 = 13
Switch_K2 = 15
Switch_K4 = 11

# Print Out Commands
print ("1 - Lampe AUS    2 - Lampe EIN ")
print ("3 - RelK2 EIN    4 - RelK2 AUS ")
print ("5 - RelK4 EIN    6 - RelK4 AUS ")
print ("7 - Read Input   8 - EXIT")

# Initialize IO
GPIO.setmode(GPIO.BOARD)
GPIO.setup (OptoIn, GPIO.IN)
GPIO.setup (Switch_K4, GPIO.OUT)
GPIO.setup (Switch_K2, GPIO.OUT)
GPIO.setup (Switch_K1, GPIO.OUT)

# Set all Ouputs OFF
GPIO.output(Switch_K1, GPIO.HIGH)
GPIO.output(Switch_K2, GPIO.HIGH)
GPIO.output(Switch_K4, GPIO.HIGH)

while 1:
    time.sleep(0.5)

    i=int(input(">"))

    if i== 1:
        GPIO.output(Switch_K1, GPIO.LOW)    # Lampe AUS
    if i== 2:
        GPIO.output(Switch_K1, GPIO.HIGH)   # Lampe EIN
    if i== 3:
        GPIO.output(Switch_K2, GPIO.LOW)    # K2 EIN
    if i== 4:
        GPIO.output(Switch_K2, GPIO.HIGH)   # K2 AUS
    if i== 5:
        GPIO.output(Switch_K4, GPIO.LOW)    # K4 EIN
    if i== 6:
        GPIO.output(Switch_K4, GPIO.HIGH)   # K4 AUS
    if i== 7:
        if GPIO.input(OptoIn)== GPIO.HIGH:
            print("b'27.4 TRUE'")
        else:
            print("b'27.4 FALSE'")
    if i== 8:        
        break

GPIO.cleanup()
print("Ciao")

        
        
