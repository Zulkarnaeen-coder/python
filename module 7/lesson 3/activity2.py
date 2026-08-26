from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("Virus scanner")
win.geometry("200x200")

def msg():
    messagebox.showwarning("Alert","Stop ! Virus detected")

btn = Button(win, text="Scan", command=msg)
btn.place(x = 40,y = 40)

win.mainloop()