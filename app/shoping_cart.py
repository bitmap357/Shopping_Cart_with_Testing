# Creating the class for the shopping cart
class ShoppingCart:
    # Defining the init function
    def __init__(self):
        self.items = {}

    # The add item function
    def add_item(self, item, quantity):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    # The remove item function
    def remove_item(self, item, quantity):
        if quantity >= self.items[item]:
            del self.items[item]
        else:
            self.items[item] -= quantity

    # The get item count function
    def get_item_count(self, item):
        if item in self.items:
            return self.items[item]
        else:
            return 0

    # The get total items function
    def get_total_items(self):
        return sum(self.items.values())

    # The get cart items function
    def get_cart_items(self):
        return list(self.items.keys())

    # The clear cart function
    def clear_cart(self):
        self.items = {}
