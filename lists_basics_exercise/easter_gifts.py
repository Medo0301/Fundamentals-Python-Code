gifts = input().split()

while True:
    command = input()
    if command == "No Money":
        break
    parts = command.split()
    the_command = parts[0]
    gift = parts[1]
    idx = int(parts[2]) if len(parts) > 2 else None

    if the_command == "OutOfStock":
        for i in range(len(gifts)):
            if gifts[i] == gift:
                gifts[i] = "None"

    elif the_command == "Required" and 0 <= idx < len(gifts):
        gifts[idx] = gift
    elif the_command == "JustInCase":
        gifts[-1] = gift

final_gifts = [gift for gift in gifts if gift != "None"]
print(" ".join(final_gifts))

# for gift in gifts:
#     if gift != "None":
#         print(gift, end=" ")


