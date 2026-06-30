def register(parking_dict: dict, the_username: str, number: str):
    if the_username in parking_dict:
        return f"ERROR: already registered with plate number {number}"
    parking_dict[the_username] = number
    return f"{the_username} registered {number} successfully"


def unregister(parking_dict: dict, the_username: str):
    if the_username not in parking_dict:
        return f"ERROR: user {the_username} not found"
    del parking_dict[the_username]
    return f"{the_username} unregistered successfully"


parking = {}
n = int(input())

for _ in range(n):
    command = input().split()
    action = command[0]
    username = command[1]

    if action == "register":
        plate_number = command[2]
        print(register(parking, username, plate_number))
    elif action == "unregister":
        print(unregister(parking, username))

for user in parking:
    print(f"{user} => {parking[user]}")
