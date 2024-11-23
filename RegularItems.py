from BaseInventoryItem import InventoryItem

class PerishableItem(InventoryItem):
    def __init__(self, name, quantity, expiry_date):
        super().__init__(name, quantity)
        self.expiry_date = expiry_date

    def __str__(self):
        return f'{self.name} (Expires: {self.expiry_date}): {self.quantity}'

# New class added for heavy items
class HeavyItem(InventoryItem):
    def __init__(self, name, quantity, weight):
        super().__init__(name, quantity)
        # Unique attribute for heavy items
        self.weight = weight

    # Sentence to be posted on inventory stock
    def __str__(self):
        return f'{self.name}: {self.quantity}. {self.weight}kg'