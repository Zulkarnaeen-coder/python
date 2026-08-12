from tkinter import *

win = Tk()
win.title("Login")
win.geometry("300x200")

frame = Frame(master=win, height=200, width=360,bg = "lightblue", fg = "white")
lb1 = Label(master=frame, text="Username", bg = "lightblue", fg = "white")
lb2 = Label(master=frame, text="Email Id", bg = "lightblue", fg = "white")
lb3 = Label(master=frame, text="Password", bg = "lightblue", fg = "white")

name = Entry(master=frame)
email = Entry(master=frame)
password = Entry(master=frame, show="*")

def display():
    nm =name.get()
    greet = "hello "+ nm +"!"
    msg = "Congratulation! You have successfully logged in."
    text_box.insert(END, greet)
    text_box.insert(END, msg)

text_box = Text(master=frame, bg = "grey",fg = "white")

btn = Button(text = "Login", command = display, bg = "lightblue", fg = "white")

frame.place(x =20,y=0)
lb1.place(x=20,y=20)
name.place(x=150,y=20)
lb2.place(x=20,y=80)
email.place(x = 150,y = 80)
lb3.place(x = 20,y = 140)
password.place(x = 150,y = 140)
btn.place(x = 150,y = 180)

text_box.place(x = 20,y = 220)

win.mainloop()