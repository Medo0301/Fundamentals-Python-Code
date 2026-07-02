contests_dict = {}
candidates = {}

while True:
    command = input()
    if command == "end of contests":
        break

    contest, password = command.split(":")
    contests_dict[contest] = password

while True:
    command = input()
    if command == "end of submissions":
        break
    contest, password, username, points = command.split("=>")
    points = int(points)

    if contest in contests_dict and password in contests_dict.values():
        if username not in candidates:
            candidates[username] = {}
        if contest not in candidates[username] or points > candidates[username][contest]:
            candidates[username][contest] = points

best_user = ""
max_point = 0
for user in candidates:
    sum_points = sum(candidates[user].values())
    if sum_points > max_point:
        best_user = user
        max_point = sum_points
print(f"Best candidate is {best_user} with total {max_point} points.")

print("Ranking:")
sorted_candidates = sorted(candidates.keys())
for user in sorted_candidates:
    print(user)
    sorted_contests = sorted(candidates[user], key=lambda contest: candidates[user][contest], reverse=True)
    for contest in sorted_contests:
        print(f"#  {contest} -> {candidates[user][contest]}")


