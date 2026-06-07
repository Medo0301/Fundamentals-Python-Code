def num_to_list_ot_digit(num: int):
    list_digit = []
    while num > 0:
        list_digit.append(num % 10)
        num = num // 10

    return list_digit


def sum_odd_even_digit(list_digit: list):
    odd_digit = []
    even_digit = []
    for digit in list_digit:
        if digit % 2 == 0:
            even_digit.append(digit)
        else:
            odd_digit.append(digit)

    return sum(even_digit), sum(odd_digit)


number = int(input())
sum_of_even_digit, sum_of_odd_digit = sum_odd_even_digit(num_to_list_ot_digit(number))

print(f"Odd sum = {sum_of_odd_digit}, Even sum = {sum_of_even_digit}")
