from tkinter import *

win = Tk()
win.title("Numbers keypad")
win.geometry("250x300")

nums = [(9,8,7),(6,5,4),(3,2,1),("#",0,"*")]

for i in range(4):
    win.columnconfigure(i, weight=1 , minsize = 75)
    win.rowconfigure(i, weight=1 , minsize = 75)

    for j in range(3):
        frame = Frame(master=win, relief=SUNKEN, borderwidth=1)
        frame.grid(row=i, column=j)
        lable = Label(master=frame, text=nums[i][j] , bg = "white")
        lable.pack(padx=5, pady=5,)

win.mainloop()