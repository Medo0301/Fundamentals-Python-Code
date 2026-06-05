list_of_numbers = [int(x) for x in input().split()]

while True:
    command = input()
    if command == "end":
        print(list_of_numbers)
        break
    if "even" in command:
        target_rem = 0
    else:
        target_rem = 1
    if "exchange" in command:
        index = int(command.split()[1])
        if 0 <= index < len(list_of_numbers):
            list_of_numbers = list_of_numbers[index + 1:] + list_of_numbers[:index + 1]
        else:
            print("Invalid index")
    elif "max" in command:
        max_value = None
        max_value_idx = -1
        for idx in range(len(list_of_numbers)):
            if list_of_numbers[idx] % 2 == target_rem and \
                    (max_value is None or list_of_numbers[idx] >= max_value):
                max_value = list_of_numbers[idx]
                max_value_idx = idx
        if max_value_idx != -1:
            print(max_value_idx)
        else:
            print("No matches")
    elif "min" in command:
        min_value = None
        min_value_idx = -1
        for idx in range(len(list_of_numbers)):
            if list_of_numbers[idx] % 2 == target_rem and \
                    (min_value is None or list_of_numbers[idx] <= min_value):
                min_value = list_of_numbers[idx]
                min_value_idx = idx
        if min_value_idx != -1:
            print(min_value_idx)
        else:
            print("No matches")
    elif "first" in command:
        count = int(command.split()[1])
        if count > len(list_of_numbers):
            print("Invalid count")
            continue
        first_target_elements = []
        for num in list_of_numbers:
            if num % 2 == target_rem:
                first_target_elements.append(num)
                if len(first_target_elements) == count:
                    break
        print(first_target_elements)

    elif "last" in command:
        count = int(command.split()[1])
        if count > len(list_of_numbers):
            print("Invalid count")
            continue
        last_target_elements = []
        for idx in range(len(list_of_numbers) - 1, -1, -1):
            if list_of_numbers[idx] % 2 == target_rem:
                last_target_elements.insert(0, list_of_numbers[idx])
                if len(last_target_elements) == count:
                    break
        print(last_target_elements)
