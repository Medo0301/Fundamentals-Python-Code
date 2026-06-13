def first_letter_decipher(code: str):
    letter_code = ""
    other_letter = ""
    for char in code:
        if char.isdigit():
            letter_code += char
        else:
            other_letter += char
    return chr(int(letter_code)) + other_letter


def cheng_second_and_last_letter(word: str):
    char_word = list(word)
    char_word[1], char_word[-1] = char_word[-1], char_word[1]
    return "".join(char_word)


code_words = input().split()
decode_words = [cheng_second_and_last_letter(first_letter_decipher(word)) for word in code_words]

print(" ".join(decode_words))
