electrons = int(input())
shells = []

while electrons > 0:
    shell_capacity = 2 * ((len(shells) + 1) ** 2)
    if shell_capacity <= electrons:
        shells.append(shell_capacity)
    else:
        shells.append(electrons)

    electrons -= shell_capacity

print(shells)
