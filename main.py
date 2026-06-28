#main
from product import Product
from product_manager import ProductManager
from cart import Cart

manager = ProductManager()

manager.add_product(Product("Laptop", 1200, 5))
manager.add_product(Product("Mouse", 25, 20))
manager.add_product(Product("Keyboard", 50, 10))

print("Products:")
manager.show_products()

print(f"\nTotal inventory value: {manager.total_inventory_value()}")


cart = Cart()

cart.add_to_cart(manager.products[0])
cart.add_to_cart(manager.products[1])
cart.add_to_cart(manager.products[2])

print("\nProducts in cart:")
cart.show_cart()

print(f"\nTotal cart value: {cart.total_price()}")