import tkinter as tk
from tkinter import messagebox

from InventoryManagement import InventoryManager
from Sections import InventorySection
from RegularItems import RegularItem, PerishableItem
from UserDetails import User 

# Predefined User for prototype:
accepted_user = User("admin1", "password1", "admin")

# Login screen
class loginScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        # Creating the actual login screen, asking user for username and password
        self.title("Login")
        self.geometry("300x150")

        tk.Label(self, text="Username:*").pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        tk.Label(self, text="Password:*").pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self, text="Login", command=self.validate_login)
        self.login_button.pack()
    
    def validate_login(self):
        # Retrieve the username and password entered by the user
        userid = self.username_entry.get()
        password = self.password_entry.get()

        # Check if the entered username and password match the stored user
        if userid == accepted_user.username and password == accepted_user.password:
            self.destroy()
            messagebox.showinfo("Login Successful", f"Welcome, {accepted_user.role.capitalize()}!")
            inventory_manager = InventoryManager() 
            inventory_manager.add_section(InventorySection("Electronics")) 
            inventory_manager.add_section(InventorySection("Automotive")) 
            app = WarehouseApp(User, inventory_manager) 
            app.mainloop() 
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

# Stock mangement screen
class WarehouseApp(tk.Tk):
    def __init__(self, user, inventory_manager):
        super().__init__()
        self.user = user
        self.inventory_manager = inventory_manager
        self.title = 'Warehouse Management System'

        self.create_widgets()
        self.update_inventory()

    def create_widgets(self):
        tk.Label(self, text='Select Section*').pack()
        self.section_var = tk.StringVar(self)
        self.section_menu = tk.OptionMenu(self, self.section_var, *self.inventory_manager.sections.keys())
        self.section_menu.pack()

        ## Item adding fields ##
        tk.Label(self, text='Item Name*').pack()
        self.add_item_name = tk.Entry(self)
        self.add_item_name.pack()

        tk.Label(self, text='Item Quantity*').pack()
        self.add_item_quantity = tk.Entry(self)
        self.add_item_quantity.pack()
        
        tk.Label(self, text='Expiry Date (DD/MM/YYYY)').pack()
        self.add_item_expiry = tk.Entry(self)
        self.add_item_expiry.pack()

        self.add_item_button = tk.Button(self, text='Add Item', command=self.add_item)
        self.add_item_button.pack()

        ## Stock management fields ##
        tk.Label(self, text='Stock Amount*').pack()
        self.stock_amount = tk.Entry(self)
        self.stock_amount.pack()

        self.add_stock_button = tk.Button(self, text='Add Stock', command=self.remove_stock)
        self.add_stock_button.pack()

        self.remove_stock_button = tk.Button(self, text='Remove Stock', command=self.remove_stock)
        self.remove_stock_button

        ## Moving stock fields ##
        tk.Label(self, text='Destination Section*').pack()
        self.move_to_var = tk.StringVar(self)
        self.move_to_section = tk.OptionMenu(self, self.move_to_var, *self.inventory_manager.sections.keys())
        self.move_to_section.pack()

        # Frame to keep dropdown and label together
        self.move_item_frame = tk.Frame(self)
        self.move_item_frame.pack()
        # Moving item label
        tk.Label(self.move_item_frame, text='Item to move*').pack()
        self.move_item_name = tk.StringVar(self)
        # Calls on function for optionMenu
        self.update_move_item_menu()


        tk.Label(self, text='QTY to move*').pack()
        self.move_amount = tk.Entry(self)
        self.move_amount.pack()
        self.move_stock_button = tk.Button(self, text='Move Stock', command=self.move_stock)
        self.move_stock_button.pack()

        ## Inventory display ##
        self.inventory_text = tk.Text(self, height = 15, width = 50)
        self.inventory_text.pack()

    def update_move_item_menu(self):
        # Checks if self already has an attribute called 'move_item_menu'
        if hasattr(self, 'move_item_menu'):
            # If it does, destroys it as it will be refreshed
            self.move_item_menu.destroy()
        # Calls 'get_all_item' function and populates all_items
        all_items = self.inventory_manager.get_all_items()
        # If all_items is empty, prints out a message
        if not all_items:
            self.move_item_menu = tk.Label(self.move_item_frame, text="No items available to move.")
        else:
            # Gets first item in all_items and sets it
            self.move_item_name.set(all_items[0])
            # Creates the dropdown menu just like for 'Destination Selector'
            self.move_item_menu = tk.OptionMenu(self.move_item_frame, self.move_item_name, *all_items)
        self.move_item_menu.pack()
    
    def add_item(self):
        section_name = self.section_var.get()
        name = self.add_item_name.get()
        quantity = int(self.add_item_quantity.get())
        if section_name and name and quantity >= 0:
            if self.add_item_expiry.get():
                item = PerishableItem(name, quantity, self.add_item_expiry.get())
            else:
                item = RegularItem(name, quantity)
            self.inventory_manager.add_item(section_name, item)
            self.update_inventory()
            self.update_move_item_menu()
        else:
            messagebox.showerror("Error", "Invalid item details")

    def add_stock(self):
        section_name = self.section_var.get()
        name = self.add_item_name.get()
        amount = int(self.stock_amount.get())
        try:
            self.inventory_manager.add_stock(section_name, name, amount)
            self.update_inventory()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def remove_stock(self):
        section_name = self.section_var.get()
        name = self.add_item_name.get()
        amount = int(self.stock_amount.get())
        try:
            self.inventory_manager.remove_stock(section_name, name, amount)
            self.update_inventory()
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    
    def move_stock(self):
        from_section_name = self.section_var.get()
        to_section_name = self.move_to_var.get()
        item_name = self.move_item_name.get()
        amount = int(self.move_amount.get())
        try:
            self.inventory_manager.move_stock(from_section_name, to_section_name, item_name, amount)
            self.update_inventory()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def update_inventory(self):
        self.inventory_text.delete(1.0, tk.END)
        inventory = self.inventory_manager.get_inventory()
        for item in inventory:
            self.inventory_text.insert(tk.END, item + '\n')
        self.update_move_item_menu()
        

# Audit log screen



if __name__ == '__main__':
    login_screen = loginScreen() 
    login_screen.mainloop()

