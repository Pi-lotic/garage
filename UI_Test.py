from Tkinter import *
from time import sleep

OUT=""

root = Tk()
var = StringVar()


def ausgabe():
    OUT=" done "
    print ("klick")
    var.set (OUT)
    


root.title ("Dem Frank sein Test")
root.geometry("100x100")

app = Frame(root)
app.grid()

button1 = Button(app, text="Garage Auf",command=ausgabe)
button1.grid()

label = Label(root, textvariable=var, relief=RAISED)
label.grid()


root.mainloop()


        


  
