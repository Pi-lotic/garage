
import sys
import os
import RPi.GPIO as GPIO
import time

mp3s = []
path ="/media/24B0-F508/"
counter =0

for x in os.listdir(path):
    if x.split(".")[1] =="mp3":
        mp3s.append(x)
        
for i in range( 0, len(mp3s)):
    print (path + mp3s[i])
    
GPIO.setmode(GPIO.BOARD)
GPIO.setup(21, GPIO.IN)

while 1:
    time.sleep(0.5)
    if counter == len(mp3s):
       counter=0

    if GPIO.input(21) == GPIO.HIGH:
        sys.stdout.write('H')
        os.system("omxplayer "+ path + mp3s[i])
        print (mp3s[i])
        counter =counter+1

    if GPIO.input(21) == GPIO.LOW:
        sys.stdout.write('L')

    else:
        sys.stdout.write('x')



        
        
