def shoot(targets_list: list, idx: int, power: int):
    targets_list[idx] -= power
    if targets_list[idx] <= 0:
        targets_list.remove(targets_list[idx])


def add(targets_list: list, idx: int, value: int):
    targets_list.insert(idx, value)


def strike(target_list: list, start: int, end: int):
    del target_list[start:end + 1]


targets = [int(x) for x in input().split()]

while True:
    command = input()
    if command == "End":
        result = [str(target) for target in targets]
        print("|".join(result))
        break
    command_parts = command.split()
    action = command_parts[0]
    index = int(command_parts[1])
    if action == "Shoot" and index in range(len(targets)):
        shoot(targets, index, int(command_parts[2]))
    elif action == "Add":
        if index in range(len(targets)):
            add(targets, index, int(command_parts[2]))
        else:
            print("Invalid placement!")
    elif action == "Strike":
        radius = int(command_parts[2])
        if index - radius >= 0 and index + radius < len(targets):
            start_radius = index - radius
            end_radius = index + radius
            strike(targets, start_radius, end_radius)
        else:
            print("Strike missed!")
