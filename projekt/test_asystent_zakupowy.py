import unittest
from models import Product, Store, Cart
import json
import os

class TestProduct(unittest.TestCase):
    def test_product_creation(self):
        p = Product("Laptop", "Elektronika", 3000.0)
        self.assertEqual(p.name, "Laptop")
        self.assertEqual(p.category, "Elektronika")
        self.assertEqual(p.price, 3000.0)


class TestStore(unittest.TestCase):
    def setUp(self):
        self.store = Store("Testowy Sklep")
        self.p1 = Product("Laptop", "Elektronika", 3000)
        self.p2 = Product("Mysz", "Elektronika", 100)
        self.p3 = Product("Książka", "Edukacja", 40)
        self.store.add_product(self.p1)
        self.store.add_product(self.p2)
        self.store.add_product(self.p3)

    def test_add_product(self):
        self.assertEqual(len(self.store.products), 3)

    def test_filter_by_category(self):
        elektronika = self.store.get_products_by_category("Elektronika")
        self.assertIn(self.p1, elektronika)
        self.assertIn(self.p2, elektronika)
        self.assertNotIn(self.p3, elektronika)

    def test_sort_by_price(self):
        sorted_products = self.store.get_sorted_products()
        self.assertEqual(sorted_products[0], self.p3)
        self.assertEqual(sorted_products[-1], self.p1)


class TestCart(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.product = Product("Laptop", "Elektronika", 3000)
        self.test_file = "test_data.json"

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_to_cart(self):
        self.cart.add_to_cart(self.product)
        self.assertIn(self.product, self.cart.items)

    def test_save_cart(self):
        self.cart.add_to_cart(self.product)
        self.cart.save_cart(self.test_file)
        with open(self.test_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.assertEqual(data[0]['name'], "Laptop")
        self.assertEqual(data[0]['category'], "Elektronika")
        self.assertEqual(data[0]['price'], 3000)


if __name__ == '__main__':
    unittest.main()