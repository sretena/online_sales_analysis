#cart
class Cart:
    def __init__(self):
        self.cart_items = []
        
    def add_to_cart(self, product):
        self.cart_items.append(product)
        
    def total_price(self):
        total = 0
        for product in self.cart_items:
            total += product.price * product.quantity
        return total
    
    def show_cart(self):
        print("Cart:")
        for product in self.cart_items:
            product.show_info()