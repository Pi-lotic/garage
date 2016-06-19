from Tkinter import *
#import Adafruit_DHT
import sys
import os
import RPi.GPIO as GPIO
import time

i=0
OptoIn    = 21
Switch_K1 = 13
Switch_K2 = 15
Switch_K4 = 11

root = Tk()
var = StringVar()

# Print Out Commands
#print ("1 - Lampe AUS    2 - Lampe EIN ")
#print ("3 - RelK2 EIN    4 - RelK2 AUS ")
#print ("5 - RelK4 EIN    6 - RelK4 AUS ")
#print ("7 - Read Input   8 - EXIT")

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

#time.sleep(0.5)
#
#print("Ciao")

def LampeAus():
        GPIO.output(Switch_K1, GPIO.LOW)    # Lampe AUS
def LampeEin():
        GPIO.output(Switch_K1, GPIO.HIGH)   # Lampe EIN
def K2Ein():
        GPIO.output(Switch_K2, GPIO.LOW)    # K2 EIN
def K2Aus():
        GPIO.output(Switch_K2, GPIO.HIGH)   # K2 AUS
def K4Ein():
        GPIO.output(Switch_K4, GPIO.LOW)    # K4 EIN
def K4Aus():
        GPIO.output(Switch_K4, GPIO.HIGH)   # K4 AUS
def EXIT():
        GPIO.cleanup()                      # EXIT
def Read(label):
    def count():
#        if GPIO.input(OptoIn)== GPIO.HIGH:
#            label.config(text=str(1))
#        else:
#            label.config(text=str(0))
        label.config(text=str(24))
        label.after(1000,count)
    count()

root.title ("Relais GUI")
root.geometry("200x400+0+20")

app = Frame(root)
app.grid()

button1 = Button(app, text="Lampe_Ein",command=LampeEin)
button1.grid()
button2 = Button(app, text="Lampe_Aus",command=LampeAus)
button2.grid()
button3 = Button(app, text="__K2_Ein",command=K2Ein)
button3.grid()
button4 = Button(app, text="__K2_Aus",command=K2Aus)
button4.grid()
button5 = Button(app, text="__K4_Ein",command=K4Ein)
button5.grid()
button6 = Button(app, text="__K4_Aus",command=K4Aus)
button6.grid()
button7 = Button(app, text="EXIT",command=EXIT)
button7.grid()


label = Label(root)
label.grid()
Read(label)

root.mainloop()


        
        
