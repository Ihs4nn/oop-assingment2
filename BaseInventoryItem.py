import logging

class InventoryItem:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def add_stock(self, amount):
        self.quantity += amount
        logging.info(f"Successfully added {amount} stock to {self.name}")

    def remove_stock(self, amount):
        if amount > self.quantity:
            raise ValueError("Not enough stock!")
        self.quantity -= amount

    def __str__(self):
        return f'{self.name}: {self.quantity}'