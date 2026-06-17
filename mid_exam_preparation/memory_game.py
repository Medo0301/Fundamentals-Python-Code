def remove_matching_elements(bord_elements: list, first_element: str, second_element: str):
    bord_elements.remove(first_element)
    bord_elements.remove(second_element)


elements = input().split()
moves = 0

while True:
    command = input()
    if command == "end":
        print("Sorry you lose :(")
        print(" ".join(elements))
        break

    moves += 1
    first_idx, second_idx = command.split()
    first_idx = int(first_idx)
    second_idx = int(second_idx)
    if first_idx == second_idx or \
            first_idx not in range(len(elements)) or \
            second_idx not in range(len(elements)):
        insert_idx = len(elements) // 2
        elements.insert(insert_idx, f"-{moves}a")
        elements.insert(insert_idx, f"-{moves}a")
        print("Invalid input! Adding additional elements to the board")
        continue

    if elements[first_idx] == elements[second_idx]:
        print(f"Congrats! You have found matching elements - {elements[first_idx]}!")
        remove_matching_elements(elements, elements[first_idx], elements[second_idx])
    else:
        print("Try again!")

    if not elements:
        print(f"You have won in {moves} turns!")
        break
