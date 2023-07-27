class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def remove_item(self, item, quantity):
        if quantity >= self.items[item]:
            del self.items[item]
        else:
            self.items[item] -= quantity