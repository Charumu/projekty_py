import unittest
import os
import json
from models import Product, Cart
from utils import load_products_from_json, save_products_to_json, sort_products, filter_products_by_category, \
    plot_products_by_category, plot_total_price_per_category


class TestShoppingAssistant(unittest.TestCase):
    def setUp(self):
        self.products = [
            Product(1, "Telefon XYZ", "Elektronika", 799.99, "SklepA"),
            Product(2, "Książka ABC", "Książki", 39.99, "Księgarnia"),
            Product(3, "Lampa LED", "Dom i ogród", 59.99, "SklepB"),
            Product(4, "Smartwatch", "Elektronika", 199.99, "SklepA"),
            Product(5, "Nożyk kuchenny", "Dom i ogród", 15.00, "SklepC")
        ]

    def test_sort_products_ascending(self):
        sorted_products = sort_products(self.products)
        self.assertEqual(sorted_products[0].name, "Książka ABC")
        self.assertEqual(sorted_products[-1].name, "Telefon XYZ")

    def test_sort_products_descending(self):
        sorted_products = sort_products(self.products, reverse=True)
        self.assertEqual(sorted_products[0].name, "Telefon XYZ")
        self.assertEqual(sorted_products[-1].name, "Książka ABC")

    def test_filter_products_by_category(self):
        filtered = filter_products_by_category(self.products, "Elektronika")
        self.assertEqual(len(filtered), 2)
        self.assertTrue(all(p.category == "Elektronika" for p in filtered))
        # test case-insensitivity
        filtered_lower = filter_products_by_category(self.products, "elektronika")
        self.assertEqual(len(filtered_lower), 2)

    def test_load_products_from_json_valid(self):
        test_data = [
            {"id": 10, "name": "Test Produkt", "category": "Test", "price": 10.5, "store_name": "TestStore"}
        ]
        filename = 'test_data_valid.json'
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(test_data, f)
        products = load_products_from_json(filename)
        self.assertEqual(len(products), 1)
        self.assertEqual(products[0].name, "Test Produkt")
        os.remove(filename)

    def test_load_products_from_json_invalid(self):
        filename = 'nonexistent.json'
        products = load_products_from_json(filename)
        self.assertEqual(products, [])

        filename2 = 'invalid_data.json'
        with open(filename2, 'w', encoding='utf-8') as f:
            json.dump([{"bad_key": 123}], f)
        products2 = load_products_from_json(filename2)
        self.assertEqual(products2, [])
        os.remove(filename2)

    def test_save_products_to_json(self):
        products = [
            Product(1, "Prod1", "Cat1", 20.0, "Store1"),
            Product(2, "Prod2", "Cat2", 30.0, "Store2")
        ]
        filename = 'test_save.json'
        save_products_to_json(products, filename)
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['name'], "Prod1")
        os.remove(filename)

    def test_cart_add_and_total(self):
        cart = Cart()
        p1 = Product(1, "Prod1", "Cat1", 15.0, "Store1")
        p2 = Product(2, "Prod2", "Cat2", 25.0, "Store2")
        cart.add_product(p1)
        cart.add_product(p2)
        self.assertEqual(len(cart.items), 2)
        self.assertAlmostEqual(cart.total_price(), 40.0)

    def test_filter_no_matches(self):
        filtered = filter_products_by_category(self.products, "Nieistniejąca")
        self.assertEqual(filtered, [])

    def test_sort_with_empty_list(self):
        self.assertEqual(sort_products([]), [])

    def test_loading_large_number_of_products(self):
        large_data = [{"id": i, "name": f"Produkt {i}", "category": "Test", "price": float(i), "store_name": "Sklep"}
                      for i in range(1000)]
        filename = 'large_data.json'
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(large_data, f)
        products = load_products_from_json(filename)
        self.assertEqual(len(products), 1000)
        os.remove(filename)

    def test_operation_on_strings(self):
        product_name = "Test Product"
        formatted = "Produkt: {}".format(product_name)
        self.assertIn("Produkt:", formatted)
        self.assertIn(product_name, formatted)

    def test_visualizations(self):
        # Wywołanie funkcji wizualizacyjnych - nie sprawdzają się w testach automatycznych,
        # ale można je wywołać, aby zobaczyć wykres
        try:
            plot_products_by_category(self.products)
            plot_total_price_per_category(self.products)
        except Exception as e:
            self.fail(f"Wizualizacja zgłosiła wyjątek: {e}")


if __name__ == '__main__':
    unittest.main()