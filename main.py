#main
from product import Product
from product_manager import ProductManager

manager = ProductManager()

manager.add_product(Product("Gaming Laptop", 1200, 3))
manager.add_product(Product("Wireless Mouse", 25, 15))
manager.add_product(Product("Mechanical Keyboard", 50, 8))

print(f"\nTotal inventory value: {manager.total_inventory_value()}")