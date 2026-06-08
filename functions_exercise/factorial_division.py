def factorial(number):
    result_ = 1
    for num in range(2, number + 1):
        result_ *= num
    return result_


first_num = int(input())
second_number = int(input())

result = factorial(first_num) / factorial(second_number)

print(f"{result:.2f}")
