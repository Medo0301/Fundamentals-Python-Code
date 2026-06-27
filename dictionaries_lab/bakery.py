elements = input().split()
bakery = {elements[idx]: int(elements[idx + 1]) for idx in range(0, len(elements), 2)}

print(bakery)
