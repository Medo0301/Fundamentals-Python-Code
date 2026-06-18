energy = int(input())
battles_count = 0

while True:
    command = input()
    if command == "End of battle":
        print(f"Won battles: {battles_count}. Energy left: {energy}")
        break

    distance = int(command)
    if energy < distance:
        print(f"Not enough energy! Game ends with {battles_count} won battles and {energy} energy")
        break
    energy -= distance
    battles_count += 1
    if battles_count % 3 == 0:
        energy += battles_count
