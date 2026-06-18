def reduce_and_increase_other_targets(targets: list, shot_target: int):
    for idx in range(len(targets)):
        if targets[idx] != -1:
            if targets[idx] <= shot_target:
                targets[idx] += shot_target
            else:
                targets[idx] -= shot_target


targets_sequence = [int(x) for x in input().split()]
count_shot_target = 0
while True:
    command = input()
    if command == "End":
        print(f"Shot targets: {count_shot_target} -> ", end="")
        print(*targets_sequence)
        break
    shoot = int(command)

    if shoot in range(len(targets_sequence)) and targets_sequence[shoot] != -1:
        target_value = targets_sequence[shoot]
        targets_sequence[shoot] = -1
        count_shot_target += 1
        reduce_and_increase_other_targets(targets_sequence, target_value)
