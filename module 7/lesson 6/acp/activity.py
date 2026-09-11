import tkinter as tk
from tkinter import ttk, messagebox
  # Requires: pip install pillow

class Stationary:
    def __init__(self, root):
        self.root = root
        self.root.title("Stationary Management App")
        self.root.geometry("800x600")

        # Menu items and prices in USD
        self.menu_items = {
            "RUBBER": 0.2,
            "PENCIL": 0.1,
            "BOOK": 1.0,
            "NOTE BOOK": 0.5,
            "RULLER": 0.5,
            "BALL PEN": 0.1
        }

        self.exchange_rate = 100  # USD to INR

        

        # Create a frame with transparency/style over the root window
        frame = ttk.Frame(self.root, padding=20)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Heading label
        ttk.Label(
            frame,
            text="Stationary Order Management",
            font=("Arial", 20, "bold")
        ).grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.menu_labels = {}
        self.menu_quantities = {}

        # Create labels and entry widgets for each menu item
        for i, (item, price) in enumerate(self.menu_items.items(), start=1):
            label = ttk.Label(
                frame,
                text=f"{item} (${price:.2f}):",
                font=("Arial", 12)
            )
            label.grid(row=i, column=0, sticky="w", padx=10, pady=5)
            self.menu_labels[item] = label

            quantity_entry = ttk.Entry(frame, width=8)
            quantity_entry.insert(0, "0")
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)
            self.menu_quantities[item] = quantity_entry

        
        self.currency_var = tk.StringVar(value="USD")
        
        ttk.Label(
            frame,
            text="Currency:",
            font=("Arial", 12)
        ).grid(row=len(self.menu_items) + 1, column=0, sticky="w", padx=10, pady=5)

        currency_dropdown = ttk.Combobox(
            frame,
            textvariable=self.currency_var,
            state="readonly",
            width=15,
            values=("USD", "BDT")
        )
        currency_dropdown.grid(
            row=len(self.menu_items) + 1,
            column=1,
            padx=10,
            pady=5
        )
        
        # Modern Tkinter variable tracking
        self.currency_var.trace_add("write", self.update_menu_prices)

        # Button to place order
        order_button = ttk.Button(
            frame,
            text="Place Order",
            command=self.place_order
        )
        order_button.grid(
            row=len(self.menu_items) + 2,
            column=0,
            columnspan=2,
            padx=10,
            pady=15
        )

        # Initialize correct label prices on load
        self.update_menu_prices()



    def update_menu_prices(self, *args):
        """Updates display labels to match current selected currency."""
        currency = self.currency_var.get()
        symbol = "৳" if currency == "BDT" else "$"
        rate = self.exchange_rate if currency == "BDT" else 1.0  

        for item, label in self.menu_labels.items():
            price = self.menu_items[item] * rate
            label.config(text=f"{item} ({symbol}{price:.2f}):")


    def place_order(self):
        """Calculates total and shows order receipt modal."""
        total_cost = 0.0
        order_summary = "Order Summary:\n" + "-" * 25 + "\n"
        currency = self.currency_var.get()
        symbol = "৳" if currency == "BDT" else "$"
        rate = self.exchange_rate if currency == "BDT" else 1.0

        for item, entry in self.menu_quantities.items():
            val = entry.get().strip()
            if val.isdigit():
                quantity = int(val)
                if quantity > 0:
                    price = self.menu_items[item] * rate
                    cost = quantity * price
                    total_cost += cost
                    order_summary += f"{item}: {quantity} x {symbol}{price:.2f} = {symbol}{cost:.2f}\n"

        if total_cost > 0:
            order_summary += "-" * 25 + f"\nTotal Cost: {symbol}{total_cost:.2f}"
            messagebox.showinfo("Order Placed", order_summary)
        else:
            messagebox.showerror("Error", "Please enter a valid quantity for at least one item.")


if __name__ == "__main__":
    root = tk.Tk()
    app = Stationary(root)
    root.mainloop()