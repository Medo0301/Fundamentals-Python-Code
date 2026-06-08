list_numbers = input().split()
list_int_numbers = []
for idx in range(len(list_numbers)):
    list_int_numbers[idx] = int(list_numbers[idx])

even_numbers = list(filter(lambda num: num % 2 == 0, list_int_numbers))

print(even_numbers)
