import socket

import time
import os


port=9991
received=""
command = (b'PLAY\n')
Temp = (b'TEMP\n')
EXIT = (b'EXIT\n')

    
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
#        os.system("omxplayer /media/24B0-F508/holztreppe.mp3")
        print (adress[0] + " : sends PLAY SONG")
        client_socket.send(b'done')
        time.sleep(0.5)
        client_socket.close()
        print("Client Socket closed")

    if data == Temp:
        print (adress[0] + " : sends Read Temp")
        client_socket.send(b'27.4')
        time.sleep(0.5)
        client_socket.close()
        print("Client Socket closed")
        
    if data == EXIT:
        print (adress[0] + " : sends EXIT Server")
        client_socket.send(b'exit')
        time.sleep(0.5)
        client_socket.close()
        print("Client Socket closed")
        server_socket.close()
        print("Server Socket closed")

        break
#    else:
#        print ("EXIT: unknown command")
    
print("Ciao")

