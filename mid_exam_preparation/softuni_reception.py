emp1_efficiency = int(input())
emp2_efficiency = int(input())
emp3_efficiency = int(input())
students_count = int(input())
needed_hours = 0
total_efficiency = emp1_efficiency + emp2_efficiency + emp3_efficiency

while students_count > 0:
    needed_hours += 1
    if needed_hours % 4 == 0:
        continue
    if students_count >= total_efficiency:
        students_count -= total_efficiency
    else:
        students_count = 0

print(f"Time needed: {needed_hours}h.")


