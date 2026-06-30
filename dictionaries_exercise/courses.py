COUNT = "count"
STUDENTS_NAME = "students"

courses = {}

while True:
    command = input()
    if command == "end":
        break

    course_name, student_name = command.split(" : ")
    if course_name not in courses:
        courses[course_name] = {COUNT: 1, STUDENTS_NAME: [student_name]}
    else:
        courses[course_name][COUNT] += 1
        courses[course_name][STUDENTS_NAME].append(student_name)

for course in courses:
    print(f"{course}: {courses[course][COUNT]}")
    for student in courses[course][STUDENTS_NAME]:
        print(f"-- {student}")
