import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# Import classes from the shop module
from src.shop import Sweet, SweetShop
import pytest


# Pytest fixture to provide a pre-populated SweetShop instance for all tests
@pytest.fixture
def shop():
    s = SweetShop()
    s.add_sweet(Sweet(1001, "Kaju Katli", "Nut-Based", 50, 20))
    s.add_sweet(Sweet(1002, "Gajar Halwa", "Vegetable-Based", 30, 15))
    s.add_sweet(Sweet(1003, "Gulab Jamun", "Milk-Based", 10, 50))
    return s

# Test to verify a new sweet can be added successfully
def test_add_sweet(shop):
    sweet = Sweet(1004, "Rasgulla", "Milk-Based", 15, 25)
    shop.add_sweet(sweet)
    assert sweet in shop.view_sweets()

# Test to ensure adding a sweet with an existing ID raises a ValueError
def test_add_duplicate_sweet(shop):
    with pytest.raises(ValueError):
        shop.add_sweet(Sweet(1001, "Duplicate", "Nut-Based", 10, 5))


# Test to verify that a sweet can be deleted and count decreases
def test_delete_sweet(shop):
    shop.delete_sweet(1002)
    assert len(shop.view_sweets()) == 2

# Test searching for a sweet by name (partial match)
def test_search_by_name(shop):
    result = shop.search_by_name("Gulab")
    assert len(result) == 1 and result[0].name == "Gulab Jamun"


# Test searching for sweets by exact category match (case-insensitive)
def test_search_by_category(shop):
    result = shop.search_by_category("Nut-Based")
    assert result[0].name == "Kaju Katli"

# Test searching for sweets within a price range
def test_search_by_price_range(shop):
    result = shop.search_by_price_range(20, 50)
    assert len(result) == 2  # Includes Kaju Katli and Gajar Halwa

# Test if sorting by name works (alphabetical order)
def test_sort_by_name(shop):
    sorted_sweets = shop.sort_by_name()
    assert sorted_sweets[0].name == "Gajar Halwa"

# Test if sorting by price returns the lowest-priced sweet first
def test_sort_by_price(shop):
    sorted_sweets = shop.sort_by_price()
    assert sorted_sweets[0].price == 10  # Gulab Jamun

# Test if purchasing reduces quantity correctly
def test_purchase_sweet(shop):
    shop.purchase_sweet(1001, 5)  # Purchase 5 units of Kaju Katli
    sweet = shop.search_by_name("Kaju Katli")[0]
    assert sweet.quantity == 15

# Test error is raised if trying to purchase more than available quantity
def test_purchase_insufficient(shop):
    with pytest.raises(ValueError):
        shop.purchase_sweet(1001, 100)


# Test if restocking increases quantity correctly
def test_restock_sweet(shop):
    shop.restock_sweet(1003, 20)  # Add 20 units to Gulab Jamun
    sweet = shop.search_by_name("Gulab Jamun")[0]
    assert sweet.quantity == 70