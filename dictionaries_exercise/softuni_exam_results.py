results = {}
submissions = {}

while True:
    command = input()
    if command == "exam finished":
        break

    command_parts = command.split("-")
    username = command_parts[0]
    if "banned" in command_parts and username in results:
        del results[username]
    else:
        language = command_parts[1]
        points = int(command_parts[2])
        if username not in results:
            results[username] = {}
        if language not in results[username] or points > results[username][language]:
            results[username][language] = points

        if language not in submissions:
            submissions[language] = 1
        else:
            submissions[language] += 1

print("Results:")
for user in results:
    print(f"{user} | {max(results[user].values())}")

print("Submissions:")
for language in submissions:
    print(f"{language} - {submissions[language]}")
