from tkinter import *
from tkinter import ttk,messagebox

class resturant:
    def __init__(self,win):
        self.win = win
        self.win.title('Resturant Management System')
        
        self.menu.list ={
            "FRIES MEAL": 2,
            "LUNCH MEAL": 2,
            "BURGER" : 3,
            "PIZZA" :4,
            "CHESSE BURGER" :2.5

        }

        self.exchange_rate = 82

        self.setup_bg(win)

        frame = ttk.Frame(win)
        frame.place(relx=0.5,rely = 0.5,anchor="tk.CENTER")

        ttk.Label(frame,text="Resturant Management System",font =("Arial",20,"bold")).grid(row = 0,columnspan = 3,pady = 20,padx = 20)

        self.menu_label = {}
        self.menu_Quantities = {}
        for i ,(item,price) in enumerate(self.menu.list.items()):
            label =ttk.Label(frame,text=f"{item} - ${price}",font =("Arial",12))
            label.grid(row = i,column = 0,pady = 5,padx =10 )

            entry = ttk.Entry(frame,width=5)
            entry.grid(row = i,column = 1,pady = 5,padx = 10)
            self.menu_Quantities[item] = entry

        self.currancy_var = Tk.StringVar()
        ttk.Label(frame,text = "Currency",font =("Arial",12)).grid(row = len(self.menu_list)+1,column =0,pady = 5,padx = 10)

        currency_dropdown = ttk.combobox(frame,textvariable = self.currancy_var,state = "readonly",values = ["USD","BDT"])

        currency_dropdown.grid(row = len(self.menu_list)+1,column = 1,pady = 5,padx = 10)

        currency_dropdown.current(0)
        self.currency_var.trace("w",self.update_currency)

        order_btn = ttk.Button(frame,text="Place Order",command = self.place_order)

        order_btn.grid(row = len(self.menu_list)+2,columnspan = 2,pady=10,padx = 10)

        #def setup_bg(self,win):




