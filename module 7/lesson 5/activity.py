from tkinter import *
from tkinter import messagebox

win = Tk()
win.geometry("600x400")
win.config(bg = "lightblue")
win.title("Denomination Calculator")

lb1 = Label(win,text = "Hey user !Welcome to the Denomination Calculator",font = ("Arial",12,"bold"),bg = "lightblue")
lb1.place(relx = 0.5,rely = 0.88,anchor = CENTER)

def msg():
    ms = messagebox.showinfo(
        "Do you want to open the calculator?",
    )
    if ms =="OK" or ms == "ok":
        topwin()

def topwin():
    tp = Toplevel(win)
    tp.geometry("600x400+50+50")
    tp.title("Denomination Calculator")
    tp.config(bg = "darkblue")


    lb2 = Label(tp,text = "Enter a amount ",bg = "light grey")
    entry = Entry(tp)

    lb3 =Label(
        tp,
        text ="Here is the notes for rach denomination",
        bg = "light grey"
    )

    lb4 = Label(tp,text = "Notes of 1000")
    lb5 = Label(tp,text = "Notes of 500")
    lb6 = Label(tp,text = "Notes of 100")

    t1 = Entry(tp)
    t2 = Entry(tp)
    t3 = Entry(tp)


    def cl():
        try:
            amount = int(entry.get())
            n1000 = amount // 1000
            n500 = (amount % 1000) // 500
            n100 = (amount % 500) // 100

            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)

            t1.insert(0,n1000)
            t2.insert(0,n500)
            t3.insert(0,n100)

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount")

    btn = Button(
        tp,text = "calculate",bg = "brown",fg = "White",command = cl
    )

    lb2.place(x =230 ,y =50)
    entry.place(x =200,y=80)
    btn.place(x = 240,y=120)

    lb3.place(x = 140,y=170)

    lb4.place(x = 180,y=230)
    lb5.place(x = 180,y=260)
    lb6.place(x = 180,y=290)
    t1.place(x = 270,y =200)
    t2.place(x = 270,y = 230)
    t3.place(x = 270,y = 260)


btn1 = Button(win,text = "Click here to open the calculator",font = ("Arial",12,"bold"),bg = "brown",command = msg )
btn1.place(x = 250,y = 360)
win.mainloop()