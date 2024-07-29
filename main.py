import tkinter as tk
from tkinter import messagebox
from business_layer import BusinessLayer

class MainForm(tk.Tk):
    def __init__(self, business_layer):
        super().__init__()
        self.business_layer = business_layer
        self.title("NorthwindApp")
        self.geometry("300x400")

        self.btn_get_customer_count = tk.Button(self, text="Get Customer Count", command=self.get_customer_count)
        self.btn_get_customer_count.pack(pady=10)

        self.btn_get_customer_names = tk.Button(self, text="Get Customer Names", command=self.get_customer_names)
        self.btn_get_customer_names.pack(pady=10)

        self.lst_customer_names = tk.Listbox(self)
        self.lst_customer_names.pack(pady=10, fill=tk.BOTH, expand=True)

    def get_customer_count(self):
        customers = self.business_layer.get_customer_data()
        messagebox.showinfo("Number of Customers", f"Number of Customers: {len(customers)}")

    def get_customer_names(self):
        customers = self.business_layer.get_customer_data()
        self.lst_customer_names.delete(0, tk.END)
        for customer in customers:
            self.lst_customer_names.insert(tk.END, customer["ContactName"])

if __name__ == "__main__":
    connection_string = (
        "Driver={SQL Server};"
        "Server=TEEJ\\SQLEXPRESS;"
        "Database=Northwind;"
        "Trusted_Connection=yes;"
    )
    bl = BusinessLayer(connection_string)
    app = MainForm(bl)
    app.mainloop()
