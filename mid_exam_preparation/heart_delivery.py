needed_hearts = [int(x) for x in input().split("@")]

cupid_position = 0
command = input()
while command != "Love!":
    jump_length = int(command.split()[1])
    cupid_position += jump_length
    if cupid_position >= len(needed_hearts):
        cupid_position = 0
    if needed_hearts[cupid_position] == 0:
        print(f"Place {cupid_position} already had Valentine's day.")
    else:
        needed_hearts[cupid_position] -= 2
        if needed_hearts[cupid_position] == 0:
            print(f"Place {cupid_position} has Valentine's day.")

    command = input()

failed_places = 0
for hearts in needed_hearts:
    if hearts > 0:
        failed_places += 1

print(f"Cupid's last position was {cupid_position}.")
if failed_places == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {failed_places} places.")
