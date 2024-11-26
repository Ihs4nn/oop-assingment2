import pytest
from InventoryManagement import InventoryManager
from Sections import InventorySection
from RegularItems import PerishableItem, HeavyItem
from UserDetails import User 
from BaseInventoryItem import InventoryItem
from UserAuthentication import validate_login

# Testing InventoryItem class
def test_add_stock():
    item = InventoryItem("TestItem", 10)
    item.add_stock(5)
    assert item.quantity == 15

    # Test for PerishableItem
    perishable_item = PerishableItem("PerishableItem", 10, "10/10/20")
    perishable_item.add_stock(5)
    assert perishable_item.quantity == 15

    # Test for HeavyItem
    heavy_item = HeavyItem("HeavyItem", 10, 20)
    heavy_item.add_stock(5)
    assert heavy_item.quantity == 15

def test_remove_stock():
    item = InventoryItem("TestItem", 10)
    item.remove_stock(5)
    assert item.quantity == 5
    with pytest.raises(ValueError):
        item.remove_stock(20)

# Testing InventoryManager class
def test_add_section():
    manager = InventoryManager()
    section = InventorySection("TestSection")
    manager.add_section(section)
    assert "TestSection" in manager.sections

def test_add_item():
    manager = InventoryManager()
    section = InventorySection("TestSection")
    manager.add_section(section)
    item = InventoryItem("TestItem", 10)
    manager.add_item("TestSection", item)
    assert "TestItem" in section.items

def test_move_stock():
    manager = InventoryManager()
    testsection1 = InventorySection("TestSection1")
    testsection2 = InventorySection("TestSection2")
    manager.add_section(testsection1)
    manager.add_section(testsection2)
    item = InventoryItem("TestItem", 10)
    manager.add_item("TestSection1", item)
    # Moving 5 of the 'TestItem' to 'TestSection2' to see if moving stock function works
    manager.move_stock("TestSection1", "TestSection2", "TestItem", 5)
    assert testsection1.items["TestItem"].quantity == 5
    assert testsection2.items["TestItem"].quantity == 5

# Testing User class
def test_user_authorisation():
    admin_user = User("admin1", "password", "admin")
    assert admin_user.authorised("add") == True
    assert admin_user.authorised("delete_all") == False

def test_user_login():
    result = validate_login("admin1", "1")
    assert result is True

# Test invalid login, wrong username
def test_invalid_username():
    result = validate_login("wronguser", "1")
    assert result is False

# Test invalid login, wrong password
def test_invalid_password():
    result = validate_login("admin1", "wrongpassword")
    assert result is False

# Test both invalid username and password
def test_invalid_credentials():
    result = validate_login("wronguser", "wrongpassword")
    assert result is False

# Testing Low stock alert
def test_low_stock_alert():
    manager = InventoryManager()
    section = InventorySection("TestSection")
    manager.add_section(section)
    # Adding test items with different quantities
    manager.add_item("TestSection", InventoryItem("TestItem1", 1))
    manager.add_item("TestSection", InventoryItem("TestItem2", 10))
    # Checking if the low quantity item is in low_stock_item list
    low_stock_items = manager.get_low_stock_items()
    assert "TestItem1" in low_stock_items
    assert "TestItem2" not in low_stock_items
