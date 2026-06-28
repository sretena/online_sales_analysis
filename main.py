#main
from product import Product
from product_manager import ProductManager

manager = ProductManager()

manager.add_product(Product("Laptop", 1200, 5))
manager.add_product(Product("Mouse", 25, 20))
manager.add_product(Product("Keyboard", 50, 10))

print("Products:")
manager.show_products()

print(f"\nTotal inventory value: {manager.total_inventory_value()}")