from models import Store, Product
from typing import List

def load_sample_data() -> List[Store]:
    store1 = Store("Sklep A")
    store1.add_product(Product("Laptop", "Elektronika", 3000))
    store1.add_product(Product("Mysz", "Elektronika", 100))

    store2 = Store("Sklep B")
    store2.add_product(Product("Laptop", "Elektronika", 2800))
    store2.add_product(Product("Mysz", "Elektronika", 120))
    store2.add_product(Product("Książka", "Edukacja", 40))

    return [store1, store2]
