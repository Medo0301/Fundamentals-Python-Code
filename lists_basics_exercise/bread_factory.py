MAX_ENERGY = 100
START_COINS = 100
REST = "rest"
ORDER = "order"

energy = MAX_ENERGY
coins = START_COINS

events = input().split("|")

for event in events:
    event_or_ingredient, number = event.split("-")
    points = int(number)

    if event_or_ingredient == REST:
        if energy + points > MAX_ENERGY:
            print(f"You gained {MAX_ENERGY - energy} energy.")
            energy = MAX_ENERGY
            print(f"Current energy: {energy}.")
        else:
            energy += points
            print(f"You gained {points} energy.")
            print(f"Current energy: {energy}.")
    elif event_or_ingredient == ORDER:
        if energy >= 30:
            print(f"You earned {points} coins.")
            coins += points
            energy -= 30
        else:
            print("You had to rest!")
            energy += 50
    else:
        if coins >= points:
            print(f"You bought {event_or_ingredient}.")
            coins -= points
        else:
            print(f"Closed! Cannot afford {event_or_ingredient}.")
            break
else:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")

