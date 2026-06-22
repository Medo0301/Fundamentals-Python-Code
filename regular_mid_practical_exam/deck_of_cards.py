def add(cards: list, new_card: str):
    if new_card in cards:
        result = "Card is already in the deck"
    else:
        cards.append(new_card)
        result = "Card successfully added"
    return result


def remove(cards: list, the_card: str):
    if the_card in cards:
        cards.remove(the_card)
        result = "Card successfully removed"
    else:
        result = "Card not found"
    return result


def remove_at(cards: list, card_idx: int):
    if card_idx in range(len(cards)):
        cards.pop(card_idx)
        result = "Card successfully removed"
    else:
        result = "Index out of range"
    return result


def insert(cards: list, card_idx: int, the_card: str):
    if card_idx not in range(len(cards)):
        result = "Index out of range"
    elif the_card in cards:
        result = "Card is already added"
    else:
        cards.insert(card_idx, the_card)
        result = "Card successfully added"
    return result


cards_deck = input().split(", ")
number = int(input())

for _ in range(number):
    command_parts = input().split(", ")
    action = command_parts[0]
    if action == "Add":
        card = command_parts[1]
        print(add(cards_deck, card))
    elif action == "Remove":
        card = command_parts[1]
        print(remove(cards_deck, card))
    elif action == "Remove At":
        index = int(command_parts[1])
        print(remove_at(cards_deck, index))
    elif action == "Insert":
        index = int(command_parts[1])
        card = command_parts[2]
        print(insert(cards_deck, index, card))

print(", ".join(cards_deck))
