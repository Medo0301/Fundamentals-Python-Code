def multiplication_sign_result(num1: int, num2: int, num3: int):
    count_negative = 0
    if num1 == 0 or num2 == 0 or num3 == 0:
        return "zero"
    if num1 < 0:
        count_negative += 1
    if num2 < 0:
        count_negative += 1
    if num3 < 0:
        count_negative += 1

    if count_negative % 2 == 0:
        return "positive"
    return "negative"


first_num = int(input())
second_num = int(input())
third_num = int(input())

result = multiplication_sign_result(first_num, second_num, third_num)
print(result)
