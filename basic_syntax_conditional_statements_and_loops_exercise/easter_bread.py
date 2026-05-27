budget = float(input())
price_kg_flour = float(input())

price_pack_eggs = price_kg_flour * 0.75
price_250_ml_milk = (price_kg_flour + price_kg_flour * 0.25) / 4

price_for_a_bread = price_kg_flour + price_pack_eggs + price_250_ml_milk

bread_count = 0
colored_eggs = 0
while budget >= price_for_a_bread:
    bread_count += 1
    colored_eggs += 3

    budget -= price_for_a_bread

    if bread_count % 3 == 0:
        colored_eggs -= (bread_count - 2)


print(f"You made {bread_count} loaves of Easter bread!"
      f" Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
