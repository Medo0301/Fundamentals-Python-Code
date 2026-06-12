numbers = list(map(int, input().split(", ")))

even_numbers_indexes = [idx for idx in range(len(numbers)) if numbers[idx] % 2 == 0]

print(even_numbers_indexes)
