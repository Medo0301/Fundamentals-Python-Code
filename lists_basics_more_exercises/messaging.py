numbers = input().split()
list_text = list(input())
message = ""

for num in numbers:
    sum_of_char = 0
    for char in num:
        sum_of_char += int(char)

    if sum_of_char >= len(list_text):
        sum_of_char = sum_of_char % len(list_text)

    message += list_text[sum_of_char]
    list_text.pop(sum_of_char)

print(message)
