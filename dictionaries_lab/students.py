students = {}
command = input()
while ":" in command:
    name, id, course = command.split(":")
    if course not in students:
        students[course] = {}
    students[course][id] = name

    command = input()

command_parts = command.split("_")
command = " ".join(command_parts)
for course in students:
    if command == course:
        for id in students[course]:
            print(f"{students[course][id]} - {id}")
