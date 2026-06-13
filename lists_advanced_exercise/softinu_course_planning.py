def swap_two_lessons(lessons: list, first_lesson: str, second_lesson: str):
    idx_first_lesson = lessons.index(first_lesson)
    idx_second_lesson = lessons.index(second_lesson)
    lessons[idx_first_lesson], lessons[idx_second_lesson] = lessons[idx_second_lesson], lessons[idx_first_lesson]


def add_exercise_for_lessons(lessons: list, exercise_: str):
    idx_lesson = lessons.index(exercise_)
    lessons.insert(idx_lesson + 1, f"{exercise_}-Exercise")


def remove_lesson(lessons: list, title: str):
    exercise_title = f"{title}-Exercise"
    lessons.remove(title)
    if exercise_title in lessons:
        lessons.remove(exercise_title)


schedule_lessons = input().split(", ")

while True:
    command = input()
    if command == "course start":
        break

    command_parts = command.split(":")
    action = command_parts[0]
    lesson_title = command_parts[1]

    if action == "Add" and lesson_title not in schedule_lessons:
        schedule_lessons.append(lesson_title)

    elif action == "Insert" and lesson_title not in schedule_lessons:
        schedule_lessons.insert(int(command_parts[2]), lesson_title)

    elif action == "Remove" and lesson_title in schedule_lessons:
        remove_lesson(schedule_lessons, lesson_title)

    elif action == "Swap" and lesson_title in schedule_lessons and command_parts[2] in schedule_lessons:
        second_lesson = command_parts[2]
        exercise_first_lesson = f"{lesson_title}-Exercise"
        exercise_second_lesson = f"{second_lesson}-Exercise"

        swap_two_lessons(schedule_lessons, lesson_title, second_lesson)

        if exercise_first_lesson in schedule_lessons and exercise_second_lesson in schedule_lessons:
            swap_two_lessons(schedule_lessons, exercise_first_lesson, exercise_second_lesson)
        elif exercise_first_lesson in schedule_lessons:
            schedule_lessons.remove(exercise_first_lesson)
            schedule_lessons.insert(schedule_lessons.index(lesson_title) + 1, exercise_first_lesson)
        elif exercise_second_lesson in schedule_lessons:
            schedule_lessons.remove(exercise_second_lesson)
            schedule_lessons.insert(schedule_lessons.index(second_lesson) + 1, exercise_second_lesson)

    elif action == "Exercise":
        exercise = f"{lesson_title}-Exercise"
        if lesson_title in schedule_lessons and exercise not in schedule_lessons:
            add_exercise_for_lessons(schedule_lessons, lesson_title)
        elif lesson_title not in schedule_lessons:
            schedule_lessons.append(lesson_title)
            schedule_lessons.append(exercise)

for idx, lesson in enumerate(schedule_lessons):
    print(f"{idx + 1}.{lesson}")
