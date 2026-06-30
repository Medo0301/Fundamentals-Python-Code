force_book_users = {}
site_order = []

while True:
    command = input()
    if command == "Lumpawaroo":
        break

    if " | " in command:
        force_side, force_user = command.split(" | ")
        if force_user not in force_book_users:
            force_book_users[force_user] = force_side
            if force_side not in site_order:
                site_order.append(force_side)
    elif " -> " in command:
        force_user, force_side = command.split(" -> ")
        if force_side not in site_order:
            site_order.append(force_side)
        if force_user in force_book_users:
            del force_book_users[force_user]
        force_book_users[force_user] = force_side
        print(f"{force_user} joins the {force_side} side!")


for side in site_order:
    members = 0
    for force_side in force_book_users.values():
        if side == force_side:
            members += 1
    if members > 0:
        print(f"Side: {side}, Members: {members}")
        for user in force_book_users:
            if force_book_users[user] == side:
                print(f"! {user}")

