def num_to_list_ot_digit(num: int):
    list_digit = []
    while num > 0:
        list_digit.append(num % 10)
        num = num // 10

    return list_digit


def sum_odd_even_digit(list_digit: list):
    even_digit_sum = 0
    odd_digit_sum = 0
    for digit in list_digit:
        if digit % 2 == 0:
            even_digit_sum += digit
        else:
            odd_digit_sum += digit

    return even_digit_sum, odd_digit_sum


number = int(input())
sum_of_even_digit, sum_of_odd_digit = sum_odd_even_digit(num_to_list_ot_digit(number))

print(f"Odd sum = {sum_of_odd_digit}, Even sum = {sum_of_even_digit}")
