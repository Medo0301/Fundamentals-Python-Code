n = int(input())
word = input()
strings = []
strings_with_word = []

for _ in range(n):
    text = input()
    strings.append(text)

print(strings)

for i  in range(n):
    element = strings[i]
    if word in element:
        strings_with_word.append(element)

print(strings_with_word)
