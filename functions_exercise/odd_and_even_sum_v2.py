def sum_odd_even_digit(list_digit: str):
    odd_digit_sum = 0
    even_digit_sum = 0
    for digit in list_digit:
        if int(digit) % 2 == 0:
            even_digit_sum += int(digit)
        else:
            odd_digit_sum += int(digit)

    return odd_digit_sum, even_digit_sum


number = input()
sum_of_even_digit, sum_of_odd_digit = sum_odd_even_digit(number)

print(f"Odd sum = {sum_of_odd_digit}, Even sum = {sum_of_even_digit}")
