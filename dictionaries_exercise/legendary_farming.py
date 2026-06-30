SHARDS = "shards"
FRAGMENTS = "fragments"
MOTES = "motes"
NEEDED_POINT = 250

items_dict = {SHARDS: 0, FRAGMENTS: 0, MOTES: 0}
legendary_item_found = False

while not legendary_item_found:
    materials = input().lower().split()
    for idx in range(0, len(materials), 2):
        quantity = int(materials[idx])
        material = materials[idx + 1]
        if material in items_dict:
            items_dict[material] += quantity
        else:
            items_dict[material] = quantity

        if material == SHARDS and items_dict[material] >= NEEDED_POINT:
            print("Shadowmourne obtained!")
            items_dict[material] -= NEEDED_POINT
            legendary_item_found = True
            break
        elif material == FRAGMENTS and items_dict[material] >= NEEDED_POINT:
            print("Valanyr obtained!")
            items_dict[material] -= NEEDED_POINT
            legendary_item_found = True
            break
        elif material == MOTES and items_dict[material] >= NEEDED_POINT:
            print("Dragonwrath obtained!")
            items_dict[material] -= NEEDED_POINT
            legendary_item_found = True
            break

for item in items_dict:
    print(f"{item}: {items_dict[item]}")
