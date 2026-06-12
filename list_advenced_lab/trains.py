def add(some_list: list, number: int):
    some_list[-1] += number
    return some_list


def insert(some_list: list, idx: int, num: int):
    some_list[idx] += num
    return some_list


def leave(some_list: list, idx: int, num: int):
    some_list[idx] -= num
    return some_list


train = [0] * int(input())

while True:
    command = input().split()
    the_command = command[0]

    if the_command == "End":
        print(train)
        break
    elif the_command == "add":
        train = add(train, int(command[1]))

    elif the_command == "insert":
        train = insert(train, int(command[1]), int(command[2]))

    elif the_command == "leave":
        train = leave(train, int(command[1]), int(command[2]))

