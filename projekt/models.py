class Product:
    def __init__(self, id, name, category, price, store_name):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.store_name = store_name

    def __repr__(self):
        return f"Product(id={self.id}, name={self.name}, category={self.category}, price={self.price}, store={self.store_name})"

class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def total_price(self):
        return sum(p.price for p in self.items)

    def __repr__(self):
        return f"Cart(items={self.items})"