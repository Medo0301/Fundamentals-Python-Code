list_numbers = input().split()
for idx in range(len(list_numbers)):
    list_numbers[idx] = int(list_numbers[idx])

even_numbers = list(filter(lambda num: num % 2 == 0, list_numbers))

print(even_numbers)
