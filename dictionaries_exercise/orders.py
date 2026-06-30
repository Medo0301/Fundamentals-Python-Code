PRICE = "price"
QUANTITY = "quantity"

orders = {}

while True:
    command = input()
    if command == "buy":
        break

    product, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)
    if product in orders:
        orders[product][PRICE] = price
        orders[product][QUANTITY] += quantity
    else:
        orders[product] = {}
        orders[product][PRICE] = price
        orders[product][QUANTITY] = quantity

for item in orders:
    total_price = orders[item][PRICE] * orders[item][QUANTITY]
    print(f"{item} -> {total_price:.2f}")