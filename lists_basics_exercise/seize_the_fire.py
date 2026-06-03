HIGH = "High"
MEDIUM = "Medium"
LOW = "Low"
HIGH_FIRE_MIN_CELL = 81
HIGH_FIRE_MAX_CELL = 125
MEDIUM_FIRE_MIN_CELL = 51
MEDIUM_FIRE_MAX_CELL = 80
LOW_FIRE_MIN_CELL = 1
LOW_FIRE_MAX_CELL = 50
EFFORT_VALUE = 0.25

fires = input().split("#")
water = int(input())
effort = 0
put_out_cells = []

for fire in fires:
    type_of_fire, cell_value = fire.split(" = ")
    cell_value = int(cell_value)
    if water >= cell_value:
        if (type_of_fire == HIGH and
                HIGH_FIRE_MIN_CELL <= cell_value <= HIGH_FIRE_MAX_CELL) or \
                (type_of_fire == MEDIUM and
                 MEDIUM_FIRE_MIN_CELL <= cell_value <= MEDIUM_FIRE_MAX_CELL) or \
                (type_of_fire == LOW and
                 LOW_FIRE_MIN_CELL <= cell_value <= LOW_FIRE_MAX_CELL):
            water -= cell_value
            effort += cell_value * EFFORT_VALUE
            put_out_cells.append(cell_value)

    if water <= 0:
        break

print("Cells:")
for cell in put_out_cells:
    print(f" - {cell}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(put_out_cells)}")
