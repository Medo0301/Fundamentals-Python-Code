COFFEE_PRICE = 1.50
WATER_PRICE = 1.00
COKE_PRICE = 1.40
SNACKS_PRICE = 2.00


def total_price(product: str, quantity: int):
    if product == "coffee":
        return COFFEE_PRICE * quantity
    elif product == "coke":
        return COKE_PRICE * quantity
    elif product == "water":
        return WATER_PRICE * quantity
    elif product == "snacks":
        return SNACKS_PRICE * quantity


product_ = input()
quantity_ = int(input())

print(f"{total_price(product_, quantity_):.2f}")
