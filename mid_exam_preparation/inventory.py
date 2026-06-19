def collect(inventory: list, new_item: str):
    inventory.append(new_item)


def drop(inventory: list, some_item: str):
    inventory.remove(some_item)


def combine_items(inventory: list, some_item: str, new_item):
    idx = inventory.index(some_item)
    inventory.insert(idx + 1, new_item)


def renew(inventory: list, some_item: str):
    inventory.remove(some_item)
    inventory.append(some_item)


items = input().split(", ")

while True:
    command = input()
    if command == "Craft!":
        print(", ".join(items))
        break
    command_parts = command.split(" - ")
    action = command_parts[0]
    item = command_parts[1]

    if action == "Collect" and item not in items:
        collect(items, item)
    elif action == "Drop" and item in items:
        drop(items, item)
    elif action == "Combine Items":
        first_item, second_item = item.split(":")
        if first_item in items:
            combine_items(items, first_item, second_item)
    elif action == "Renew" and item in items:
        renew(items, item)
