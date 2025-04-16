class Product:
    def __init__(self, name, product_id, price, quantity,category,manufacturer):
        self.name = name
        self.product_id = product_id
        self.price = price
        self.quantity = quantity

    def add_stock(self, quantity):
        self.quantity += quantity
        print(f"Added {quantity} units to {self.name}. New stock: {self.quantity}")

    def remove_stock(self, quantity):
        if self.quantity >= quantity:
            self.quantity -= quantity
            print(f"Removed {quantity} units from {self.name}. Remaining stock: {self.quantity}")
            return True
        else:
            print(f"Not enough stock for {self.name}. Available: {self.quantity}")
            return False

    def view_stock(self):
        print(f"{self.name} - Stock: {self.quantity}")


class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.product_id] = product
        print(f"Added product: {product.name} (ID: {product.product_id})")

    def list_products(self):
        print("\nInventory:")
        for product in self.products.values():
            print(f"{product.name} (ID: {product.product_id}) - Stock: {product.quantity}")


class Sales:
    def __init__(self, inventory):
        self.inventory = inventory

    def sell_product(self, product_id, quantity):
        if product_id in self.inventory.products:
            product = self.inventory.products[product_id]
            if product.remove_stock(quantity):
                total_price = quantity * product.price
                print(f"Sold {quantity} units of {product.name}. Total: ${total_price}")
                return total_price
        else:
            print("Product not found.")
            return 0

    def generate_invoice(self, product_id, quantity):
        total = self.sell_product(product_id, quantity)
        if total > 0:
            print(f"Invoice: {quantity} x {self.inventory.products[product_id].name} = ${total}")


# Example usage
inventory = Inventory()

# Adding products
p1 = Product("Laptop", 101, 800, 10)
p2 = Product("Phone", 102, 500, 20)
p3=Product("Androied",233,30000,10)

inventory.add_product(p1)
inventory.add_product(p2)
inventory.add_product(p3)

# Viewing inventory
inventory.list_products()

# Selling a product
sales = Sales(inventory)
sales.generate_invoice(101, 2)  # Selling 2 laptops

# Viewing updated stock
p1.view_stock()
