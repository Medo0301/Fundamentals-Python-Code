MAX_HEALTH = 100

dungeons_rooms = input().split("|")
health = MAX_HEALTH
total_bitcoins = 0
rooms_count = 0

for room in dungeons_rooms:
    rooms_count += 1
    command, number = room.split()
    if command == "potion":
        hp = int(number)
        if health < MAX_HEALTH and hp > MAX_HEALTH - health:
            hp = MAX_HEALTH - health
            health = MAX_HEALTH
        else:
            health += hp
        print(f"You healed for {hp} hp.")
        print(f"Current health: {health} hp.")
    elif command == "chest":
        bitcoins = int(number)
        total_bitcoins += bitcoins
        print(f"You found {bitcoins} bitcoins.")
    else:
        monster = command
        attack = int(number)
        health -= attack
        if health > 0:
            print(f"You slayed {monster}.")
        else:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {rooms_count}")
            break
else:
    print(f"You've made it!\nBitcoins: {total_bitcoins}\nHealth: {health}")

