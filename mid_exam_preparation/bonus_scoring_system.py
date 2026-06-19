from math import ceil

students = int(input())
course_lectures = int(input())
additional_bonus = int(input())
max_bonus = 0
max_student_attendances = 0

for _ in range(students):
    student_attendances = int(input())
    student_bonus = student_attendances / course_lectures * (5 + additional_bonus)
    if student_bonus > max_bonus:
        max_bonus = student_bonus
        max_student_attendances = student_attendances

print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {max_student_attendances} lectures.")