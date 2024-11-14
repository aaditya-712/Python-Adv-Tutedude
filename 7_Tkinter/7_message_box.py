# step1: import tkinter
from tkinter import *
import tkinter.messagebox

# step2: gui interaction
window = Tk()

# step3: adding input
window.title("Message Box")

# tkinter.messagebox.showinfo("Info", "showinfo")
# tkinter.messagebox.showwarning("Info", "showwarning")
# tkinter.messagebox.showerror("Info", "showerror")

question = tkinter.messagebox.askyesno("Weather", "Will it rain tomorrow?")
# tkinter.messagebox.askokcancel("askokcancel", "Do you want to go further?")
# tkinter.messagebox.askretrycancel("trycancel", "error")
# tkinter.messagebox.askyesnocancel("askyesnocancel", "Yes No Cancel")
# tkinter.messagebox.askquestion("askquestion", "Yes No")

if question == True:
    print("Take an umbrela")
else:
    print("okay")

# step4: mainloop
mainloop()