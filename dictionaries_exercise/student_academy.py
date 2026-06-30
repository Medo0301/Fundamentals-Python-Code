MIN_AVERAGE_GRADE = 4.50

number_of_students = int(input())
students_grades = {}

for _ in range(number_of_students):
    students_name = input()
    grade = float(input())

    if students_name not in students_grades:
        students_grades[students_name] = [grade]
    else:
        students_grades[students_name].append(grade)

for student in students_grades:
    average_grade = sum(students_grades[student]) / len(students_grades[student])
    if average_grade >= MIN_AVERAGE_GRADE:
        print(f"{student} -> {average_grade:.2f}")
