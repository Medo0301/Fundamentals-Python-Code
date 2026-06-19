def fire(ship: list, idx: int, damage: int):
    ship[idx] -= damage


def defend(ship: list, star: int, end: int, damage: int):
    for idx in range(star, end + 1):
        ship[idx] -= damage


def repair(ship: list, idx: int, health: int):
    ship[idx] += health


pirate_ship_status = [int(x) for x in input().split(">")]
warship_status = [int(x) for x in input().split(">")]

max_health_section = int(input())
is_stalemate = True

while True:
    command = input()
    if command == "Retire":
        break
    command_parts = command.split()
    action = command_parts[0]

    if action == "Fire":
        index = int(command_parts[1])
        if index in range(len(warship_status)):
            fire(warship_status, index, int(command_parts[2]))
            if warship_status[index] <= 0:
                print("You won! The enemy ship has sunken.")
                is_stalemate = False
                break
    elif action == "Defend":
        start_idx = int(command_parts[1])
        end_idx = int(command_parts[2])
        if start_idx in range(len(pirate_ship_status)) \
                and end_idx in range(len(pirate_ship_status)) \
                and start_idx < end_idx:
            defend(pirate_ship_status, start_idx, end_idx, int(command_parts[3]))
            if min(pirate_ship_status) <= 0:
                print("You lost! The pirate ship has sunken.")
                is_stalemate = False
                break
    elif action == "Repair":
        index = int(command_parts[1])
        if index in range(len(pirate_ship_status)):
            repair(pirate_ship_status, index, int(command_parts[2]))
            if pirate_ship_status[index] > max_health_section:
                pirate_ship_status[index] = max_health_section
    elif action == "Status":
        count = 0
        for section in pirate_ship_status:
            if section < max_health_section * 0.2:
                count += 1
        print(f"{count} sections need repair.")


if is_stalemate:
    print(f"Pirate ship status: {sum(pirate_ship_status)}")
    print(f"Warship status: {sum(warship_status)}")
