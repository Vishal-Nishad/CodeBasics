import pytest
from inventory_management import Inventory

def test_add_stock():
    inv=Inventory()
    inv.add_stock("widget",5)
    assert inv.stock["widget"]==5
    inv.add_stock("widget",8)
    assert inv.stock["widget"]==13

def test_remove_stock():
    inv=Inventory()
    inv.add_stock("widget",15)
    inv.remove_stock("widget",8)
    assert inv.stock["widget"]==7
    with pytest.raises(ValueError):
        inv.remove_stock("widget",8)
        # should raise an error coz only 7 left

def test_check_availability():
    inv=Inventory()
    inv.add_stock("widget",5)
    assert inv.check_availability("widget",3) is True


def test_remove_stock_with_insufficient_inventory():
    inv = Inventory()
    inv.add_stock("widget", 2)
    with pytest.raises(ValueError):
        inv.remove_stock("widget", 3)  # More than in stock
def test_full_inventory_cycle():
    inv = Inventory()
    inv.add_stock("widget", 10)
    inv.remove_stock("widget", 4)
    assert inv.check_availability("widget", 6) is True
    inv.remove_stock("widget", 6)
    assert inv.check_availability("widget", 1) is False