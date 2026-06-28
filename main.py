#main
from product import Product
from product_manager import ProductManager
from cart import Cart

manager = ProductManager()

manager.add_product(Product("Gaming Laptop", 1200, 3))
manager.add_product(Product("Wireless Mouse", 25, 15))
manager.add_product(Product("Mechanical Keyboard", 50, 8))

print(f"\nTotal inventory value: {manager.total_inventory_value()}")


cart = Cart()

cart.add_to_cart(manager.products[0])
cart.add_to_cart(manager.products[1])
cart.add_to_cart(manager.products[2])

print("\nProducts in cart:")
cart.show_cart()

print(f"\nTotal cart value: {cart.total_price()}")