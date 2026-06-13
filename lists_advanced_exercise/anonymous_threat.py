def merge_command(the_message: list, start: int, end: int) -> list:
    if start < 0 or start >= len(the_message):
        start = 0
    if end >= len(the_message) or end < 0:
        end = len(the_message) - 1
    elements_in_range = the_message[start: end + 1:]
    the_message = [the_message[idx] for idx in range(len(the_message)) if not (start <= idx <= end)]
    the_message.insert(start, "".join(elements_in_range))
    return the_message


def divide_command(the_message: list, index: int, partitions: int) -> list:
    part = len(the_message[index]) // partitions
    element_for_divide = the_message.pop(index)
    divided_element = []
    current_idx = 0
    for _ in range(partitions - 1):
        divided_element.append(element_for_divide[current_idx: current_idx + part])
        current_idx += part
    # divided_element = [element_for_divide[i: i + part] for i in range(0, len(element_for_divide) - part, part)]
    divided_element.append(element_for_divide[current_idx:])
    the_message = the_message[:index] + divided_element + the_message[index:]
    return the_message


message = input().split()

while True:
    command = input().split()
    if command[0] == "3:1":
        break
    elif command[0] == "merge":
        message = merge_command(message, int(command[1]), int(command[2]))

    elif command[0] == "divide":
        message = divide_command(message, int(command[1]), int(command[2]))

print(" ".join(message))
