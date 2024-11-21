import logging
from RegularItems import RegularItem, PerishableItem

class InventorySection:
    def __init__(self, name):
        self.name = name
        self.items = {}
    
    def add_item(self, item):
        self.items[item.name] = item

    def get_item(self, name):
        return self.items.get(name)
    
    def add_stock(self, name, amount, misc_info = None, exp_date = None):
        item = self.get_item(name)
        if item:
            item.add_stock(amount)
        else:
            if misc_info == "p":
                item = PerishableItem(name, 0, exp_date)
            else: 
                item = RegularItem(name, 0)
        
        self.add_item(item)
        item.add_stock(amount)

    def remove_stock(self, name, amount):
        item = self.get_item(name)
        if item:
            try:
                item.remove_stock(amount)
            except ValueError as e:
                raise ValueError(e)
        else:
            raise ValueError('Item not found')
        

    def __str__(self):
        return f'Section: {self.name}'