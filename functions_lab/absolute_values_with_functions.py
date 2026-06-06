def convert_strings_to_floats(strings_lists: list):
    floats_list = []
    for item in strings_lists:
        floats_list.append(float(item))
    return floats_list


def get_absolute_values(numbers_list: list):
    absolute_list = []
    for num in numbers_list:
        absolute_list.append(abs(num))
    return absolute_list


strings_input_list = input().split()

final_list = get_absolute_values(convert_strings_to_floats(strings_input_list))
print(final_list)
