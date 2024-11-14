# step1: import tkinter
from tkinter import *

# step2: gui interaction
window = Tk()

# step3: adding input
window.title("Menu bar")
window.geometry("500x500")

menu = Menu(window)
file = Menu(menu, tearoff=0)
file.add_command(label="New")
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Save as")
file.add_separator()
file.add_command(label="Print..")
file.add_separator()
file.add_command(label="Exit", command=window.quit)

menu.add_cascade(label="File", menu=file)
window.config(menu=menu)

# step4: main loop
mainloop()