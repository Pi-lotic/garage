import socket
import time
import os

host = "192.168.2.107"
print (host)
port=9999
received=""

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket made")

client_socket.connect((host,port))
print("Socket connected")

data = client_socket.recv(512)
print (data)
command = (b'CMD')
print (command)
if data == command:
    os.system("omxplayer /media/24B0-F508/holztreppe.mp3")
    print ("Hab es")

else:
    print ("unknown command")

