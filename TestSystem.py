import pytest

from InventoryManagement import InventoryManager
from Sections import InventorySection
from RegularItems import PerishableItem, HeavyItem
from UserDetails import User 
from BaseInventoryItem import InventoryItem

# Testing InventoryItem class
def test_add_stock():
    item = InventoryItem("TestItem", 10)
    item.add_stock(5)
    assert item.quantity == 15

def test_remove_stock():
    item = InventoryItem("TestItem", 10)
    item.remove_stock(5)
    assert item.quantity == 5
    with pytest.raises(ValueError):
        item.remove_stock(20)

# Testing InventoryManager class
