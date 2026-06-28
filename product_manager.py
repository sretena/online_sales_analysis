#product_manager
from product import Product

class ProductManager:
    def __init__(self):
        self.products = []
        
    def add_product(self, product):
        self.products.append(product)
        
    def show_products(self):
        for product in self.products:
            product.show_info()
            
    def total_inventory_value(self):
        total = 0
        for product in self.products:
            total += product.price * product.quantity
        return total
    
    def remove_product(self, name):
        self.products = [
            product for product in self.products
            if product.name != name
        ]
        
