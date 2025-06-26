from utils import load_sample_data
from models import Cart

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
            fname = "data.json"
            cart.save_cart(fname)
            print("Zapisano koszyk do pliku data.json.")

        elif choice == 6:
            print("Do widzenia!")
            break

        else:
            print("Niepoprawna opcja.")

if __name__ == "__main__":
    main()
