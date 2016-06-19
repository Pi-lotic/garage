
import sys
import os
import RPi.GPIO as GPIO
import time
i=0
GateMoving = 21
MoveGate = 11
StopGate = 13

def inputLow(GateMoving):
    print("Event")
    GPIO.output(StopGate, GPIO.LOW)

print ("1-START_GATE 2-STOP_GATE 3-ON 4-OFF 5-READ 6-EXIT")
GPIO.setmode(GPIO.BOARD)
GPIO.setup(GateMoving, GPIO.IN)
GPIO.add_event_detect(GateMoving, GPIO.FALLING, callback=inputLow, bouncetime=1000)
GPIO.setup(MoveGate, GPIO.OUT)
GPIO.setup(StopGate, GPIO.OUT)


while 1:
    time.sleep(0.5)

    i=int(input(">"))

    if i== 1:
        GPIO.output(MoveGate, GPIO.LOW)
    if i== 2:
        GPIO.output(MoveGate, GPIO.HIGH)
    if i== 3:
        GPIO.output(StopGate, GPIO.LOW)
    if i== 4:
        GPIO.output(StopGate, GPIO.HIGH)
    if i== 5:
        print("")
    if i== 6:
        break

GPIO.cleanup()
print("Ciao")

        
        
