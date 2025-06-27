from models import Product, Cart
from utils import (
    load_products_from_json,
    save_products_to_json,
    sort_products,
    filter_products_by_category,
    plot_products_by_category,
    plot_total_price_per_category
)


def display_products(products):
    for p in products:
        print(p)


def main():
    filename = 'products.json'
    products = load_products_from_json(filename)

    # Jeśli plik nie istnieje lub jest pusty, tworzymy przykładowe dane
    if not products:
        products = [
            Product(1, "Laptop ABC", "Elektronika", 1200.0, "SklepX"),
            Product(2, "Książka DEF", "Książki", 45.0, "KsięgarniaY"),
            Product(3, "Odkurzacz", "Dom i ogród", 300.0, "SklepZ"),
            Product(4, "Smartphone", "Elektronika", 800.0, "SklepX"),
            Product(5, "Mata do jogi", "Sport", 50.0, "SklepSport")
        ]
        save_products_to_json(products, filename)

    cart = Cart()

    while True:
        print("\n--- MENU ---")
        print("1. Wyświetl produkty")
        print("2. Posortuj produkty")
        print("3. Filtruj produkty po kategorii")
        print("4. Dodaj produkt do koszyka")
        print("5. Wyświetl koszyk")
        print("6. Wykonaj wizualizacje")
        print("0. Wyjście")
        choice = input("Wybierz opcję: ")

        if choice == '1':
            print("\nLista produktów:")
            display_products(products)

        elif choice == '2':
            order = input("Wybierz kolejność (asc/desc): ").lower()
            reverse = (order == 'desc')
            sorted_products = sort_products(products, reverse=reverse)
            print("\nPosortowane produkty:")
            display_products(sorted_products)

        elif choice == '3':
            category = input("Podaj nazwę kategorii do filtrowania: ")
            filtered = filter_products_by_category(products, category)
            print(f"\nProdukty w kategorii '{category}':")
            display_products(filtered)

        elif choice == '4':
            try:
                product_id = int(input("Podaj ID produktu do dodania do koszyka: "))
                product = next((p for p in products if p.id == product_id), None)
                if product:
                    cart.add_product(product)
                    print(f"Produkt {product.name} dodany do koszyka.")
                else:
                    print("Nie znaleziono produktu o podanym ID.")
            except ValueError:
                print("Niepoprawne ID.")

        elif choice == '5':
            print("\nZawartość koszyka:")
            for item in cart.items:
                print(item)
            print(f"Razem: {cart.total_price():.2f}")

        elif choice == '6':
            print("\nWykonanie wizualizacji...")
            try:
                plot_products_by_category(products)
                plot_total_price_per_category(products)
            except Exception as e:
                print(f"Wystąpił błąd podczas wizualizacji: {e}")

        elif choice == '0':
            print("Koniec programu.")
            break

        else:
            print("Nieprawidłowa opcja, spróbuj ponownie.")


if __name__ == "__main__":
    main()