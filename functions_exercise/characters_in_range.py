def characters_in_range(char_1: str, char_2: str):
    result = []
    for idx in range(ord(char_1) + 1, ord(char_2)):
        result.append(chr(idx))

    return " ".join(result)


char1 = input()
char2 = input()

print(characters_in_range(char1, char2))
