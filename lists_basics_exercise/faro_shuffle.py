deck = input().split()

count_shuffles = int(input())

for _ in range(count_shuffles):
    middle = len(deck) // 2
    first_half_deck = deck[:middle]
    second_half_deck = deck[middle:]
    deck.clear()
    for idx in range(len(first_half_deck)):
        deck.append(first_half_deck[idx])
        deck.append(second_half_deck[idx])

print(deck)
