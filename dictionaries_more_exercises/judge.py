judge_exercises = {}
standings = {}

while True:
    command = input()
    if command == "no more time":
        break

    username, contest, points = command.split(" -> ")
    points = int(points)
    if contest not in judge_exercises:
        judge_exercises[contest] = {}
    if username not in standings:
        standings[username] = 0
    if username not in judge_exercises[contest]:
        standings[username] += points
        judge_exercises[contest][username] = points
    elif points > judge_exercises[contest][username]:
        standings[username] += (points - judge_exercises[contest][username])
        judge_exercises[contest][username] = points

for task in judge_exercises:
    sort_users = sorted(judge_exercises[task].keys())
    final_sort_users = sorted(sort_users, key=lambda the_user: judge_exercises[task][the_user], reverse=True)
    print(f"{task}: {len(judge_exercises[task])} participants")
    place = 0
    for user in final_sort_users:
        place += 1
        print(f"{place}. {user} <::> {judge_exercises[task][user]}")

sorted_users = sorted(standings.keys())
final_sorted_users = sorted(sorted_users, key=lambda the_user: standings[the_user], reverse=True)
print("Individual standings:")
position = 0
for user in final_sorted_users:
    position += 1
    print(f"{position}. {user} -> {standings[user]}")
