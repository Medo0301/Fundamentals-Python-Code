def loot(new_items: list, treasure_chest: list):
    for item in new_items:
        if item not in treasure_chest:
            treasure_chest.insert(0, item)


def drop(treasure_chest: list, idx: int):
    dropped_item = treasure_chest.pop(idx)
    treasure_chest.append(dropped_item)


def steal(treasure_chest: list, count: int):
    all_stolen_items = []
    for _ in range(count):
        if treasure_chest:
            steal_item = treasure_chest.pop()
            all_stolen_items.insert(0, steal_item)
        else:
            break
    print(", ".join(all_stolen_items))


items_in_chest = input().split("|")

while True:
    command = input()
    if command == "Yohoho!":
        break
    command_parts = command.split()
    action = command_parts[0]

    if action == "Loot":
        command_parts.remove(action)
        loot(command_parts, items_in_chest)
    elif action == "Drop":
        index = int(command_parts[1])
        if index in range(len(items_in_chest)):
            drop(items_in_chest, index)
    elif action == "Steal":
        steal(items_in_chest, int(command_parts[1]))

if not items_in_chest:
    print("Failed treasure hunt.")
else:
    total_items_len = 0
    count_items = 0
    for item in items_in_chest:
        total_items_len += len(item)
        count_items += 1
    average_gain = total_items_len / count_items
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")

