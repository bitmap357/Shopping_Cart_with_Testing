from app.shoping_cart import ShoppingCart
import pytest


def test_add_item():
    cart = ShoppingCart()
    cart.add_item("apple", 2)
    assert cart.get_item_count("apple") == 2
    assert cart.get_total_items() == 2
