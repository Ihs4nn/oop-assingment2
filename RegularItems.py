from BaseInventoryItem import InventoryItem
import logging

class RegularItem(InventoryItem):
    def add_stock(self, amount):
        self.quantity += amount
        logging.info(f"Successfully added {amount} stock to {self.name}")

    def remove_stock(self, amount):
        if amount > self.quantity:
            raise ValueError("Not enough stock!")
        self.quantity -= amount


class PerishableItem(InventoryItem):
    def __init__(self, name, quantity, expiry_date):
        super().__init__(name, quantity)
        self.expiry_date = expiry_date

    def add_stock(self, amount):
        self.quantity += amount
        logging.info(f'Successfully added {amount} stock to {self.name}')

    def remove_stock(self, amount):
        if amount > self.quantity:
            raise ValueError("Not enough stock!")
        self.quantity -= amount

    def __str__(self):
        return f'{self.name} (Expires: {self.expiry_date}): {self.quantity}'