def urgent(list_of_items: list, new_item: str):
    list_of_items.insert(0, new_item)


def unnecessary(list_of_items: list, item_for_remove: str):
    list_of_items.remove(item_for_remove)


def correct(list_of_items: list, old_item: str, new_item: str):
    idx = list_of_items.index(old_item)
    list_of_items[idx] = new_item


def rearrange(list_of_items: list, target_item: str):
    unnecessary(list_of_items, target_item)
    list_of_items.append(target_item)


shopping_list = input().split("!")

while True:
    command = input()
    if command == "Go Shopping!":
        print(", ".join(shopping_list))
        break
    command_parts = command.split()
    action = command_parts[0]
    item = command_parts[1]
    if action == "Urgent" and item not in shopping_list:
        urgent(shopping_list, item)
    elif action == "Unnecessary" and item in shopping_list:
        unnecessary(shopping_list, item)
    elif action == "Correct" and item in shopping_list:
        correct(shopping_list, item, command_parts[2])
    elif action == "Rearrange" and item in shopping_list:
        rearrange(shopping_list, item)
