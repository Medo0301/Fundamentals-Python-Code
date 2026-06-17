TAXES_PERCENT = 0.20
SPECIAL_DISCOUNT = 0.10

total_price = 0.0
customer_type = ""
total_taxes = 0.0

while True:
    received_value = input()
    if received_value == "special" or received_value == "regular":
        customer_type = received_value
        break
    price = float(received_value)
    if price < 0:
        print("Invalid price!")
        continue
    total_price += price
    total_taxes += (price * TAXES_PERCENT)

if total_price == 0:
    print("Invalid order!")
else:
    final_price = total_price + total_taxes
    if customer_type == "special":
        final_price -= final_price * SPECIAL_DISCOUNT
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {total_price:.2f}$\nTaxes: {total_taxes:.2f}$\n-----------")
    print(f"Total price: {final_price:.2f}$")
