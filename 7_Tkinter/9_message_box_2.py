# import tkinter
from tkinter import *

# gui interaction
window = Tk()

#adding input
window.geometry("500x500")

# message = Message(window, text="Python")
# message.pack()

# var = StringVar()
# message = Message(window, textvariable = var, relief=RAISED, padx=20, pady=20)
# var.set("Welcome")
# message.pack()

var = StringVar()
ent_var = StringVar()

def insert():
    result = ent_var.get()
    var.set(result)

message = Message(window, textvariable = var, pady=50, padx=50, relief=RAISED)
entry = Entry(window, textvariable = ent_var)
button = Button(window, text="OK", command=insert)

message.pack()
entry.pack()
button.pack()
# mainloop
mainloop()