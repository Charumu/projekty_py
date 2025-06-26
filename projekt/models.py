import json
from typing import List

class Product:
    def __init__(self, name: str, category: str, price: float):
        self.name = name
        self.category = category
        self.price = price

    def __repr__(self):
        return f"{self.name} ({self.category}): {self.price:.2f} zł"


class Store:
    def __init__(self, name: str):
        self.name = name
        self.products: List[Product] = []

    def add_product(self, product: Product):
        self.products.append(product)

    def get_products_by_category(self, category: str):
        return [p for p in self.products if p.category.lower() == category.lower()]

    def get_sorted_products(self):
        return sorted(self.products, key=lambda p: p.price)


class Cart:
    def __init__(self):
        self.items: List[Product] = []

    def add_to_cart(self, product: Product):
        self.items.append(product)

    def save_cart(self, filename: str):
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump([vars(p) for p in self.items], f, indent=4, ensure_ascii=False)
        except IOError as e:
            print("Błąd zapisu pliku:", e)
