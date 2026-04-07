class Product:
    def __init__(self, product_id, name, price, in_stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.in_stock = in_stock

    def __str__(self):
        status = "In Stock" if self.in_stock else "Out of Stock"
        return f"[{self.product_id}] {self.name} - ${self.price:.2f} ({status})"

    def __repr__(self):
        return (f"Product(product_id={self.product_id!r}, name={self.name!r}, "
                f"price={self.price!r}, in_stock={self.in_stock!r})")


# --- Usage ---

p = Product("Logitech-101", "Wireless Mouse", 29.99, True)

# __str__ → for display, logs, UI output
print(p)
# [Logitech-101] Wireless Mouse - $29.99 (In Stock)
print("---")
# __repr__ → for debugging, REPL, error logs
print(repr(p))
# Product(product_id='Logitech-101', name='Wireless Mouse', price=29.99, in_stock=True)

# Inside a list → __repr__ is used automatically

inventory = [
    Product("Logitech-101", "Wireless Mouse", 29.99, True),
    Product("Logitech-202", "USB Hub", 15.49, False),
]
print("Inventory --")
print(inventory)
