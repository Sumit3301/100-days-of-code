#creating GUI in python with tkinter
#basics of tkinter

import tkinter
from tkinter import font
from tkinter import *

window=tkinter.Tk()
window.title("This is a window")

window.minsize(width=200,height=200)## default size

#label

label1=tkinter.Label(text="kilometer to Miles Converter",font=("Arial",24,"bold"))
label1.grid(row=0,column=1)

#button 
label2=tkinter.Label(text=" ", font=("Arial",10,"bold"))
label2.grid(row=5,column=1)
#entry

input=Entry()


def clicked():
    str=input.get()
    print(str)

    label2.config(text=int(str)*0.621371)
    
button=Button(text="Click Here",command=clicked)
button.grid(row=4,column=1)
# without pack, place and grid widget wont be shown
input.grid(row=3,column=1)


window.mainloop() #keeping window on the screen