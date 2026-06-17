WAGON_CAPACITY = 4

people_on_the_queue = int(input())
lift_wagons = list(map(int, input().split()))

for idx in range(len(lift_wagons)):
    if lift_wagons[idx] < WAGON_CAPACITY:
        free_seats = WAGON_CAPACITY - lift_wagons[idx]
        if people_on_the_queue >= free_seats:
            lift_wagons[idx] += free_seats
            people_on_the_queue -= free_seats
        else:
            lift_wagons[idx] += people_on_the_queue
            people_on_the_queue = 0
    if people_on_the_queue <= 0:
        break

empty_seats = len(lift_wagons) * WAGON_CAPACITY - sum(lift_wagons)
if people_on_the_queue <= 0 and empty_seats == 0:
    print(*lift_wagons)
elif people_on_the_queue > 0:
    print(f"There isn't enough space! {people_on_the_queue} people in a queue!")
    print(*lift_wagons)
elif empty_seats > 0:
    print("The lift has empty spots!")
    print(*lift_wagons)
