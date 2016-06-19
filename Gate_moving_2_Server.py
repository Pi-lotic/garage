
import socket
import sys
import os
import RPi.GPIO as GPIO
import time
i=0
OptoIn    = 21
Switch_K1 = 13
Switch_K2 = 15
Switch_K4 = 11

MoveGateSTA = 0
port        = 9992
received    = ""


command = (b'PLAY\n')
Temp = (b'TEMP\n')
EXIT = (b'EXIT\n')

# Initialize IO
GPIO.setmode(GPIO.BOARD)
GPIO.setup (OptoIn, GPIO.IN)
GPIO.setup (Switch_K4, GPIO.OUT)
GPIO.setup (Switch_K2, GPIO.OUT)
GPIO.setup (Switch_K1, GPIO.OUT)

# Set all Ouputs
GPIO.output(Switch_K1, GPIO.HIGH)
GPIO.output(Switch_K2, GPIO.LOW)
GPIO.output(Switch_K4, GPIO.HIGH)

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
        if MoveGateSTA == 0:
            GPIO.output(Switch_K1, GPIO.LOW)
            MoveGateSTA = 1
        else:
            GPIO.output(Switch_K1, GPIO.HIGH)
            MoveGateSTA = 0            
        
#    if i== 2:
#        GPIO.output(MoveGate, GPIO.HIGH)

#    if i== 3:
#        GPIO.output(StopGate, GPIO.LOW)

#    if i== 4:
#        GPIO.output(StopGate, GPIO.HIGH)

    if data == Temp:
        print (adress[0] + " : sends Read Input")
        if GPIO.input(OptoIn)== GPIO.HIGH:
            client_socket.send(b'27.4 TRUE')
        else:
            client_socket.send(b'27.4 FALSE')
        time.sleep(0.5)
        client_socket.close()
        print("Client Socket closed")

        
    if data == EXIT:
        print (adress[0] + " : sends EXIT Server")
        client_socket.close()
        print("Client Socket closed")
        server_socket.close()
        print("Server Socket closed")
        break

GPIO.cleanup()
print("Ciao")

        
        
