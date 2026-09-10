from tkinter import *
from tkinter import messagebox

win = Tk()
win.geometry("500x300")
win.config(bg="lightblue")
win.title("Redaing Scheduler Planner")

h = Label(
    win,text = "Reading Scheduler Planner",font = ("Arial",18,"bold"),bg = "lightblue",fg = "White"
)
h.pack(pady =50)

def msg():
    ms = messagebox.showinfo(text ="Do you want to open the calculator?"
    )
    if ms == "OK" or ms == "ok":
        topwin()


def topwin():
    tp = Toplevel(win)
    tp.geometry("500x350+50+50")
    tp.title("Create Reading Plan")
    tp.config(bg="darkblue")

    pg_l = Label(tp, text="Enter total number of pages ", bg="light grey")
    pg_entry = Entry(tp)

    daily_l = Label(tp, text="Enter pages that you can read each day", bg="light grey")
    daily_pg_ent = Entry(tp)

    result_l = Label(tp, text="Your Reading Plan", font=("Arial", 14, "bold"), bg="light grey")

    d_l = Label(tp, text="Complete reading days", bg="light grey")

    remaining_l = Label(tp, text="Pages remaining", bg="light grey")

    days_ent = Entry(tp)
    remaining_ent = Entry(tp)

    def cl():
        try:
            tt_pg = int(pg_entry.get())
            daily_pg = int(daily_pg_ent.get())

            if tt_pg <= 0 or daily_pg <= 0:
                messagebox.showerror(
                    "Invalid Input", "Please enter numbers greater than zero."
                )

            cmp_d = tt_pg // daily_pg
            rem_pg = tt_pg % daily_pg

            days_ent.delete(0, END)
            remaining_ent.delete(0, END)

            days_ent.insert(END, str(cmp_d))
            remaining_ent.insert(END, str(rem_pg))

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")

    cl_btn = Button(tp, text="Calculate", bg="brown", fg="White", command=cl)
    pg_l.place(x=80, y=40)
    pg_entry.place(x=280, y=40)

    daily_l.place(x=80, y=90)
    daily_pg_ent.place(x=280, y=90)

    cl_btn.place(x=205, y=135)
    result_l.place(x=175, y=185)

    d_l.place(x=80, y=235)
    days_ent.place(x=280, y=235)

    remaining_l.place(x=80, y=275)
    remaining_ent.place(x=280, y=275)


start_button = Button(
    win, text="Create My Reading Plan", command=topwin, bg="#1261A0", fg="white"
)
start_button.pack(pady=15)

win.mainloop()
