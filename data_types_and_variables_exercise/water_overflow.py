WATER_TANK_CAPACITY = 255

n = int(input())
liters_in_tank = 0

for _ in range(n):
    liters_of_water = int(input())
    if liters_in_tank + liters_of_water <= WATER_TANK_CAPACITY:
        liters_in_tank += liters_of_water
    else:
        print("Insufficient capacity!")

print(liters_in_tank)
