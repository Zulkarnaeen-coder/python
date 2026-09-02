from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

win = Tk()
win.geometry("500x600")
win.title("Codingal's text editor")

win.rowconfigure(0,minsize =800,weight=1)
win.columnconfigure(0,minsize =800,weight=1)

def open():
    fp = askopenfilename(title="Open file",filetypes=(("Text files","*.txt"),("All files","*.*")))
    if not fp:
        return
    textedit.delete(1.0,END)

    with open(fp,"r") as file:
        text = file.read()
        textedit.delete(1.0,END)
        textedit.insert(1.0,text)

    win.title(f"Codingal's text editor - {fp}")

def save():
    fp = asksaveasfilename(title="Save file",defaultextension=".txt",filetypes=(("Text files","*.txt"),("All files","*.*")))
    if not fp:
        return
    with open(fp,"w") as otfile:
        text = textedit.get(1.0,END)
        otfile.write(text)
    win.title(f"Codingal's text editor - {fp}")

textedit = Text(win)

fr_btn = Frame(win, relief=RAISED, bd=2)
btn_open = Button(fr_btn, text="Open", command=open)
btn_save = Button(fr_btn, text="Save As", command=save)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_btn.grid(row=0, column=0, sticky="ns")
win.mainloop()