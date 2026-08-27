from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("After school routine checker")
win.geometry("400x320")

heading = Label(win, text="My After-School Routine", font=("Arial", 16, "bold"))
heading.pack(pady=10)

inst = Label(win, text="Enter your next after-school task:")
inst.pack()

task_inp = Entry(win, width=35)
task_inp.pack(pady=8)

key = Label(text = "Last key pressed: None")
key.pack(pady=5)

def  key_press(event):
    key.config(text = "Last key pressed: " + event.char)

def click(event):
    routine.config(text = "Routine area selected!")

routine = Label(win, text="Click here to check your routine", bg="#d0efff", width=32, height=3)
routine.pack(pady=10)

routine.bind("<Button-1>", click)

def check_routine():
    task = task_inp.get()

    if task == "":
        messagebox.showwarning("Missing Task", "Please enter an after-school task.")
    else:
        routine.config(text="Next task: " + task)

task_inp.bind("<Key>", key_press)

btn = Button(win, text="Check Routine", command=check_routine)

btn.pack(pady=10)

win.mainloop()