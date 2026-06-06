def calculations(operator: str, first_num: int, second_num: int):
    if operator == "add":
        return add(first_num, second_num)
    elif operator == "subtract":
        return subtract(first_num, second_num)
    elif operator == "multiply":
        return multiply(first_num, second_num)
    elif operator == "divide" and second_num != 0:
        return divide(first_num, second_num)


def add(a: int, b: int):
    return a + b


def subtract(a: int, b: int):
    return a - b


def multiply(a: int, b: int):
    return a * b


def divide(a: int, b: int):
    if b == 0:
        return "Can't divide by zero"
    else:
        return int(a / b)


operator_ = input()
num_1 = int(input())
num_2 = int(input())

print(calculations(operator_, num_1, num_2))