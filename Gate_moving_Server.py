
import socket
import sys
import os
import RPi.GPIO as GPIO
import time
i=0
GateMoving  = 21
SwitchK2    = 15
MoveGate    = 11
MoveGateSTA = 0
StopGate    = 13
port        = 9990
received    = ""


command = (b'PLAY\n')
Temp = (b'TEMP\n')
EXIT = (b'EXIT\n')
print ("1-START_GATE 2-STOP_GATE 3-ON 4-OFF 5-READ 6-EXIT")

GPIO.setmode(GPIO.BOARD)
GPIO.setup(GateMoving, GPIO.IN)
GPIO.setup(MoveGate , GPIO.OUT)
GPIO.setup(StopGate , GPIO.OUT)
GPIO.setup(SwitchK2 , GPIO.OUT)

GPIO.output(MoveGate, GPIO.HIGH)
GPIO.output(StopGate, GPIO.HIGH)
GPIO.output(SwitchK2, GPIO.HIGH)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket made")

server_socket.bind(("",port))
print("Socket Bound")

server_socket.listen(1)
print("Listening for connections...")

while 1:
    client_socket,adress = server_socket.accept()
    print ("Connected with " + adress[0] + " : " + str(adress[1]))

    data = client_socket.recv(512)
    print (data)

    if data == command:
        print (adress[0] + " : sends Start Gate")
        client_socket.send(b'done')
        time.sleep(0.5)
        client_socket.close()
        print("Client Socket closed")
        GPIO.output(SwitchK2, GPIO.HIGH)
        if MoveGateSTA == 0:
            GPIO.output(MoveGate, GPIO.LOW)
            MoveGateSTA = 1
        else:
            GPIO.output(MoveGate, GPIO.HIGH)
            MoveGateSTA = 0            
        time.sleep(0.5)
        GPIO.output(SwitchK2, GPIO.LOW)
        
#    if i== 2:
#        GPIO.output(MoveGate, GPIO.HIGH)

#    if i== 3:
#        GPIO.output(StopGate, GPIO.LOW)

#    if i== 4:
#        GPIO.output(StopGate, GPIO.HIGH)

    if data == Temp:
        print (adress[0] + " : sends Read Input")
        if GPIO.input(GateMoving)== GPIO.HIGH:
            client_socket.send(b'27.4 TRUE')
        else:
            client_socket.send(b'27.4 FALSE')
        time.sleep(0.5)
        client_socket.close()
        print("Client Socket closed")
        GPIO.output(StopGate, GPIO.HIGH) 
        time.sleep(0.5)
        GPIO.output(StopGate, GPIO.LOW) 
        
    if data == EXIT:
        print (adress[0] + " : sends EXIT Server")
        client_socket.close()
        print("Client Socket closed")
        server_socket.close()
        print("Server Socket closed")
        break

GPIO.cleanup()
print("Ciao")

        
        
