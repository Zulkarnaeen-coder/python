from tkinter import *

win = Tk()
win.title(" ATM pin Login")
win.geometry("400x500")

dfm = Frame(master = win, height = 150, width = 360 ,bg = "#d0efff")

lbn = Label(master = dfm, text = "Account Name", bg = "#3895D3", fg = "white", width = 14)
lbp = Label(master = dfm, text = "Create PIN", bg = "#3895D3", fg = "white", width = 14)

inpn = Entry(master = dfm)
inpp = Entry(master = dfm, show = "*")

def conf_pin():
    pin = inpp.get()
    acc_name = inpn.get()
    msg_box.delete(1.0, END)
    if (pin == "") or (acc_name == ""):
        msg_box.delete(1.0, END)
        msg_box.insert(END, "Please enter the account name and PIN.")

    else:
        msg = "Hello " + acc_name + "\nYour ATM PIN has been set successfully."
        msg_box.insert(END, msg)

msg_box = Text(win,height =5,wid = 42,bg = "#BEBEBE",fg = "black")

key_frame = Frame(master = win,relief = SUNKEN,borderwidth = 2)

nums = [(1,2,3),(4,5,6),(7,8,9),("Clear",0,"Enter")]

for i in range(4):
    key_frame.rowconfigure(i, weight = 1, minsize = 40)
    for j in range(3):
        key_frame.columnconfigure(j, weight = 1, minsize = 70)
        cell = Frame(master = key_frame, relief = RAISED, borderwidth = 1)
        cell.grid(row = i, column = j, sticky = "nsew")
        num_label = Label(master = cell, text = nums[i][j], bg = "#d0efff")
        num_label.pack(padx = 8, pady = 8)

conf_btn = Button(win, text = "Set ATM PIN", command = conf_pin, bg = "red", fg = "white")

dfm.place(x = 20, y = 10)
lbn.place(x = 15, y = 25)
lbp.place(x = 15, y = 65)
inpn.place(x = 150, y = 25)
inpp.place(x = 150, y = 65)
msg_box.place(x = 20, y = 200)
key_frame.place(x = 20, y = 280)
conf_btn.place(x = 150, y = 450)

win.mainloop()