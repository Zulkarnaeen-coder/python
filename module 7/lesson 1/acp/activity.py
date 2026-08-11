from datetime import date
from tkinter import *

win = Tk()
win.title("Workshop Participant Greeting")
win.geometry("400x300")

lb = Label(
    win,
    text="Workshop Welcome Desk",
    fg="white",
    bg="#072F5F",
    height=1,
    width=300,
)
lb.pack()


name_entry = Entry(win, fg="White", bg="Blue")
name_entry.pack(pady=5)


def display():
    name = name_entry.get()
    text_box.delete(1.0, END)
    greet = "Hello " + name + "!\n"
    msg = "Welcome to the workshop.\n"

   
    today_str = "Date: " + str(date.today())

    text_box.insert(END, greet)
    text_box.insert(END, msg)
    text_box.insert(END, today_str)


text_box = Text(win, height=4, width=40)
btn = Button(win,text="Check In",command=display, height=1,bg="#1261A0",fg="white",)

btn.pack(pady=10)
text_box.pack()

win.mainloop()
