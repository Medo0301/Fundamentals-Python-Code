# Mutate Strings - Solved without using lists
# Achieved using only string slicing and loops

first_str = input()
second_str = input()

for idx in range(len(first_str)):
    result_text = ""

    if first_str[idx] != second_str[idx]:
        result_text += second_str[:idx + 1] + first_str[idx + 1:]
        print(result_text)
