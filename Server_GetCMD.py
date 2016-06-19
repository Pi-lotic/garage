import socket

import time
import os


port=9990
received=""
command = (b'PLAY\n')
EXIT = (b'EXIT')


while 1:

    time.sleep(0.5)
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket made")

    server_socket.bind(("",port))
    print("Socket Bound")

    server_socket.listen(1)
    print("Listening for connections...")

    client_socket,adress = server_socket.accept()
    print ("Connected with " + adress[0] + " : " + str(adress[1]))

    data = client_socket.recv(512)
    print (data)

    if data == command:
#        os.system("omxplayer /media/24B0-F508/holztreppe.mp3")
        print (adress[0] + " : sends PLAY SONG")
        server_socket.close()
        print("Server Socket closed")
        client_socket.close()
        print("Client Socket closed")

    if data == EXIT:
        print (adress[0] + " : sends EXIT Server")
        break
#    else:
#        print ("EXIT: unknown command")
    
server_socket.close()
print("Server Socket closed")
client_socket.close()
print("Client Socket closed")

