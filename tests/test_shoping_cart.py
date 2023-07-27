from app.shoping_cart import ShoppingCart
import pytest


def test_add_item():
    cart = ShoppingCart()
    cart.add_item("apple", 2)
    assert cart.get_item_count("apple") == 2
    assert cart.get_total_items() == 2


def test_remove_item():
    cart = ShoppingCart()
    cart.add_item("apple", 3)
    cart.remove_item("apple", 2)
    assert cart.get_item_count("apple") == 1
    assert cart.get_total_items() == 1


def test_get_cart_items():
    cart = ShoppingCart()
    cart.add_item("apple", 2)
    cart.add_item("banana", 3)
    items = cart.get_cart_items()
    assert "apple" in items
    assert "banana" in items
