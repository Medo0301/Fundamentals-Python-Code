number_of_chars = int(input())
ascii_sum = 0

for _ in range(number_of_chars):
    latter = input()
    ascii_sum += ord(latter)

print(f"The sum equals: {ascii_sum}")
