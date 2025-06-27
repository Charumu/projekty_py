import json
from models import Product
from collections import defaultdict, Counter
import matplotlib.pyplot as plt

def load_products_from_json(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        products = []
        for item in data:
            try:
                product = Product(
                    id=item['id'],
                    name=item['name'],
                    category=item['category'],
                    price=float(item['price']),
                    store_name=item['store_name']
                )
                products.append(product)
            except (KeyError, ValueError, TypeError):
                continue
        return products
    except FileNotFoundError:
        return []

def save_products_to_json(products, filename):
    data = []
    for p in products:
        data.append({
            'id': p.id,
            'name': p.name,
            'category': p.category,
            'price': p.price,
            'store_name': p.store_name
        })
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def sort_products(products, reverse=False):
    return sorted(products, key=lambda p: p.name, reverse=reverse)

def filter_products_by_category(products, category):
    category_lower = category.lower()
    return [p for p in products if p.category.lower() == category_lower]

# Funkcje wizualizacyjne
def plot_products_by_category(products):
    from collections import Counter
    categories = [product.category for product in products]
    category_counts = Counter(categories)

    labels = list(category_counts.keys())
    counts = list(category_counts.values())

    plt.figure(figsize=(10,6))
    plt.bar(labels, counts, color='skyblue')
    plt.xlabel('Kategoria')
    plt.ylabel('Liczba produktów')
    plt.title('Ilość produktów w poszczególnych kategoriach')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_total_price_per_category(products):
    from collections import defaultdict
    category_totals = defaultdict(float)
    for p in products:
        category_totals[p.category] += p.price

    labels = list(category_totals.keys())
    totals = list(category_totals.values())

    plt.figure(figsize=(10,6))
    plt.bar(labels, totals, color='lightgreen')
    plt.xlabel('Kategoria')
    plt.ylabel('Suma cen')
    plt.title('Suma cen w poszczególnych kategoriach')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()