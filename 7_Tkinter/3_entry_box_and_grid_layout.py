# ENTRY BOX AND GRID LAYOUT

# Step1: import tkinter
from tkinter import *

# Step2: gui interaction
window = Tk()

# Step3: adding input
window.title("Simple")
window.geometry("400x100")

label1 = Label(text="Mail")
label2 = Label(text="Password")

e1 = Entry(window, width=40, borderwidth=5)
e2 = Entry(window, width=40, borderwidth=5)

label1.grid(row=0, column=1)
label2.grid(row=1, column=1 )
e1.grid(row=0, column=2)
e2.grid(row=1, column=2)

# Step4: main loop
mainloop()