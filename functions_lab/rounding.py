def round_numbers(list_of_strings: list):
    rounded_list = []
    for item in list_of_strings:
        rounded_list.append(round(float(item)))

    return rounded_list


list_strings = input().split()

print(round_numbers(list_strings))
