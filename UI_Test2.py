from tkinter import *
from time import sleep



root = Tk()
var = StringVar()
counter = 0

def ausgabe():
    OUT=" done "
    print ("klick")
    var.set (OUT)

def temperatur(label):
    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000,count)
    count()
        


root.title ("Dem Frank sein Test")
root.geometry("200x400+0+20")

app = Frame(root)
app.grid()

button1 = Button(app, text="Garage Auf",command=ausgabe)
button1.grid()

label = Label(root)
label.grid()
temperatur(label)

root.mainloop()


        


  
