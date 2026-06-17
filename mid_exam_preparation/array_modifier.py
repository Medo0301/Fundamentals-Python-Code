def swap(array: list, first_idx: int, second_idx: int):
    array[first_idx], array[second_idx] = array[second_idx], array[first_idx]


def multiply(array: list, first_idx: int, second_idx: int):
    array[first_idx] *= array[second_idx]


def decrease(array: list):
    decrease_array = [(x - 1) for x in array]
    return decrease_array


integers_array = [int(x) for x in input().split()]

while True:
    command = input()
    if command == "end":
        break
    command_parts = command.split()
    action = command_parts[0]
    if len(command_parts) > 1:
        idx1 = int(command_parts[1])
        idx2 = int(command_parts[2])
    if action == "swap":
        swap(integers_array, idx1, idx2)
    elif action == "multiply":
        multiply(integers_array, idx1, idx2)
    elif action == "decrease":
        integers_array = decrease(integers_array)

str_array = [str(x) for x in integers_array]
print(", ".join(str_array))
