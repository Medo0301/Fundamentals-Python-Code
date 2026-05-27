# Since the input structure is guaranteed, words are identified
# solely by their length, without using lists or string methods.

queue = " " + input()
sheep_count = 0
letter_count = 0

for idx in range(len(queue) - 1, -1, -1):

    if queue[idx] == " ":
        if letter_count == 4 and sheep_count == 0:
            print("Please go away and stop eating my sheep")
            break
        elif letter_count == 4 and sheep_count != 0:
            print(f"Oi! Sheep number {sheep_count}! You are about to be eaten by a wolf!")
            break
        elif letter_count == 5:
            sheep_count += 1
            letter_count = 0
    elif queue[idx] == ",":
        continue
    else:
        letter_count += 1
