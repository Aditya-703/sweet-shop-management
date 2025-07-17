import pytest

# Import classes from the shop module
from src.shop import Sweet, SweetShop

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

