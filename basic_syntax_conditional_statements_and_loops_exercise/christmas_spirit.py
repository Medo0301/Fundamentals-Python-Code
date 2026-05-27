ORNAMENT_SET_PRICE = 2
TREE_SKIRT_PRICE = 5
TREE_GARLAND_PRICE = 3
TREE_LIGHTS_PRICE = 15
ORNAMENT_SET_POINTS = 5
TREE_SKIRT_POINTS = 3
TREE_GARLAND_POINTS = 10
TREE_LIGHTS_POINTS = 17
TREE_LIGHTS_AND_GARLANDS_BONUS_POINTS = 30
CAT_RUINS_TREE_DECOR_LOSE_POINTS = 20
CAT_RUINS_TURKEY_LOSE_POINTS = 30

quantity = int(input())
days = int(input())

total_cost = 0
total_spirit = 0

for day in range(1, days + 1):

    if day % 11 == 0:
        quantity += 2

    if day % 2 == 0:
        total_cost += ORNAMENT_SET_PRICE * quantity
        total_spirit += ORNAMENT_SET_POINTS

    if day % 3 == 0:
        total_cost += (TREE_SKIRT_PRICE * quantity
                       + TREE_GARLAND_PRICE * quantity)
        total_spirit += (TREE_SKIRT_POINTS + TREE_GARLAND_POINTS)

    if day % 5 == 0:
        total_cost += TREE_LIGHTS_PRICE * quantity
        if day % 3 == 0:
            total_spirit += TREE_LIGHTS_POINTS + TREE_LIGHTS_AND_GARLANDS_BONUS_POINTS
        else:
            total_spirit += TREE_LIGHTS_POINTS

    if day % 10 == 0:
        total_spirit -= CAT_RUINS_TREE_DECOR_LOSE_POINTS
        total_cost += (TREE_SKIRT_PRICE + TREE_GARLAND_PRICE + TREE_LIGHTS_PRICE)

    if day == days and day % 10 == 0:
        total_spirit -= CAT_RUINS_TURKEY_LOSE_POINTS

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")
