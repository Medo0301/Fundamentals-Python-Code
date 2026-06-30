text = input()
chars_counter = {}

for char in text:
    if char != " ":
        if char not in chars_counter:
            chars_counter[char] = 1
        else:
            chars_counter[char] += 1

for char in chars_counter:
    print(f"{char} -> {chars_counter[char]}")

