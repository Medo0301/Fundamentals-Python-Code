def num_to_list_ot_digit(str_num: str):
    list_digit = []
    for digit in str_num:
        list_digit.append(int(digit))

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


number = input()
sum_of_even_digit, sum_of_odd_digit = sum_odd_even_digit(num_to_list_ot_digit(number))

print(f"Odd sum = {sum_of_odd_digit}, Even sum = {sum_of_even_digit}")
