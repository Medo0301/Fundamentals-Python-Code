TRAIN_TICKET_TO_FRANCE = 150
MARKUP = 0.4
CLOTHES_MAX_PRICE = 50.0
SHOES_MAX_PRICE = 35.0
ACCESSORIES_MAX_PRICE = 20.50

items = input().split("|")
budget = int(input())
prices = []
profit = 0

for item in items:
    type_item, price = item.split("->")
    price = float(price)
    if budget >= price:
        if (type_item == "Clothes" and price <= CLOTHES_MAX_PRICE) or\
                (type_item == "Shoes" and price <= SHOES_MAX_PRICE) or\
                (type_item == "Accessories" and price <= ACCESSORIES_MAX_PRICE):
            budget -= price
            profit += price * MARKUP
            price += price * MARKUP
            prices.append(price)

formatted_prices = [f"{price:.2f}" for price in prices]
print(" ".join(formatted_prices))
print(f"Profit: {profit:.2f}")
if budget + sum(prices) > TRAIN_TICKET_TO_FRANCE:
    print("Hello, France!")
else:
    print("Not enough money.")
