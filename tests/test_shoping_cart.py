from app.shoping_cart import ShoppingCart
import pytest


def test_add_item():
    cart = ShoppingCart()
    cart.add_item("apple", 2)
