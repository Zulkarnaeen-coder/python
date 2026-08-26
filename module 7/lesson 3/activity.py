from tkinter import *

win = Tk()
win.geometry("200x200")

def press(event):
    print(event.char)

win.bind("<Key>", press)

def key_press(event):
    print("button pressed:")

win.bind("<Button-1>", key_press)

btn = Button(win, text="Click me")
btn.pack()

win.mainloop()