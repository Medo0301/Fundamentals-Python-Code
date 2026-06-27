elements = input().split()
products_to_chek = input().split()

stocks = {elements[idx]: int(elements[idx + 1]) for idx in range(0, len(elements), 2)}

for product in products_to_chek:
    if product in stocks:
        print(f"We have {stocks[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")

