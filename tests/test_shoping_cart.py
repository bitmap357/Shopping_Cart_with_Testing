from app.shoping_cart import ShoppingCart
import pytest


# The decorator for fixtures and the function to hold the shopping cart object
@pytest.fixture
def cart():
    return ShoppingCart()


# The function to test the add item
def test_add_item(cart):
    cart.add_item("apple", 2)
    assert cart.get_item_count("apple") == 2
    assert cart.get_total_items() == 2


# The function to test the remove item
def test_remove_item(cart):
    cart.add_item("apple", 3)
    cart.remove_item("apple", 2)
    assert cart.get_item_count("apple") == 1
    assert cart.get_total_items() == 1


def test_get_cart_items(cart):
    cart.add_item("apple", 2)
    cart.add_item("banana", 3)
    items = cart.get_cart_items()
    assert "apple" in items
    assert "banana" in items


def test_clear_cart(cart):
    cart.add_item("apple", 2)
    cart.clear_cart()
    assert cart.get_total_items() == 0
    assert cart.get_cart_items() == []
