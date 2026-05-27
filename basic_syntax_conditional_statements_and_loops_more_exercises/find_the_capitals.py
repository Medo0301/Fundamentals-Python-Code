# Find the Capitals - Solved without using lists (avoiding the hint)
# Formatted manually using print flags and end parameters


text = input()

print("[", end="")
is_first = True
for idx in range(len(text)):
    char = text[idx]

    if char.isupper():
        if not is_first:
            print(", ", end="")
        print(idx, end="")
        is_first = False

print("]")
