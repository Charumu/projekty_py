import json
from typing import List, Dict

# -----------------------
# MODELE
# -----------------------

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

# -----------------------
# KOSZYK
# -----------------------https://cdn.discordapp.com/attachments/725789917694918857/1385640094874210354/kVkBMfL.mp4?ex=6856cd66&is=68557be6&hm=cbadd0002d041a7a1d59e2fd88422bfbfde6fef0d4ee9f24b4adecd9148d19b0&

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

# -----------------------
# FUNKCJE POMOCNICZE
# -----------------------

def load_sample_data() -> List[Store]:
    store1 = Store("Sklep A")
    store1.add_product(Product("Laptop", "Elektronika", 3000))
    store1.add_product(Product("Mysz", "Elektronika", 100))

    store2 = Store("Sklep B")
    store2.add_product(Product("Laptop", "Elektronika", 2800))
    store2.add_product(Product("Mysz", "Elektronika", 120))
    store2.add_product(Product("Książka", "Edukacja", 40))

    return [store1, store2]

# -----------------------
# INTERFEJS TEKSTOWY
# -----------------------

def main():
    stores = load_sample_data()
    cart = Cart()

    while True:
        print("\n1. Pokaż wszystkie produkty")
        print("2. Filtruj po kategorii")
        print("3. Sortuj po cenie")
        print("4. Dodaj produkt do koszyka")
        print("5. Zapisz koszyk do pliku")
        print("6. Wyjdź")

        try:
            choice = int(input("Wybierz opcję: "))
        except ValueError:
            print("Niepoprawny wybór. Wpisz cyfrę.")
            continue

        if choice == 1:
            for store in stores:
                print(f"\n{store.name}:")
                for p in store.products:
                    print(" -", p)

        elif choice == 2:
            cat = input("Podaj kategorię: ")
            for store in stores:
                filtered = store.get_products_by_category(cat)
                if filtered:
                    print(f"\n{store.name}:")
                    for p in filtered:
                        print(" -", p)

        elif choice == 3:
            for store in stores:
                sorted_products = store.get_sorted_products()
                print(f"\n{store.name}:")
                for p in sorted_products:
                    print(" -", p)

        elif choice == 4:
            name = input("Podaj nazwę produktu do dodania: ").lower()
            found = False
            for store in stores:
                for p in store.products:
                    if p.name.lower() == name:
                        cart.add_to_cart(p)
                        print(f"Dodano {p.name} do koszyka.")
                        found = True
                        break
                if found:
                    break
            if not found:
                print("Nie znaleziono produktu.")

        elif choice == 5:
            fname = input("Podaj nazwę pliku (np. koszyk.json): ")
            cart.save_cart(fname)
            print("Zapisano koszyk.")

        elif choice == 6:
            print("Do widzenia!")
            break

        else:
            print("Niepoprawna opcja.")

if __name__ == "__main__":
    main()
