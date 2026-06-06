def calculations(operator: str, first_num: int, second_num: int):
    if operator == "add":
        return first_num + second_num
    elif operator == "subtract":
        return first_num - second_num
    elif operator == "multiply":
        return first_num * second_num
    elif operator == "divide" and second_num != 0:
        return int(first_num / second_num)


operator_ = input()
num_1 = int(input())
num_2 = int(input())

print(calculations(operator_, num_1, num_2))
