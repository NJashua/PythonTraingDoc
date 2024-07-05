class JythonShoppee:
    def __init__(self):
        self.cart_items = []

    def add_cart(self, item_name, quantity):
        self.cart_items.append((item_name, quantity))
        print("Item added into cart")

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item[0] == item_name:
                self.cart_items.remove(item)
                print("Item deleted successfully")
                break

    def calculate_total(self):
        total_quantity = sum(quantity for item_name, quantity in self.cart_items)
        print("Total quantity is: ", total_quantity)


shop = JythonShoppee()
shop.add_cart("Papaya", 200)
shop.add_cart("Apple", 50)
#  shop.remove_item("Papaya")
shop.calculate_total()

print(shop.cart_items)