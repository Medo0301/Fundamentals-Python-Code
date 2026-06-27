inventory = {}

while True:
    command = input()
    if command == "statistics":
        break

    kay, value = command.split(": ")
    if kay in inventory:
        inventory[kay] += int(value)
    else:
        inventory[kay] = int(value)

print("Products in stock:")
for product in inventory:
    print(f"- {product}: {inventory[product]}")

print(f"Total Products: {len(inventory.keys())}")
print(f"Total Quantity: {sum(inventory.values())}")
