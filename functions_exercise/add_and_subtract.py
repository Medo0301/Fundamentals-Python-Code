def sum_numbers(num1: int, num2: int):
    return num1 + num2


def subtract(num1: int, num2: int):
    return num1 - num2


def add_and_subtract(num1: int, num2: int, num3: int):
    return subtract(sum_numbers(num1, num2), num3)


first_num = int(input())
second_num = int(input())
third_num = int(input())

print(add_and_subtract(first_num, second_num, third_num))
