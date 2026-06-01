total_persons = int(input())
elevator_capacity = int(input())

if total_persons % elevator_capacity == 0:
    courses = total_persons // elevator_capacity
else:
    courses = total_persons // elevator_capacity + 1

print(courses)
