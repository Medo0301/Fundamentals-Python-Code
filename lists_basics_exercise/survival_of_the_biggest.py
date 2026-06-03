numbers = [int(x) for x in input().split()]
numbers_to_remove = int(input())

for _ in range(numbers_to_remove):
    min_num = min(numbers)
    numbers.remove(min_num)

print(*numbers, sep=", ")

