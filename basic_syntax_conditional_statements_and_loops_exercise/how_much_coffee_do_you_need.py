COFFEE_LIMIT = 5

coffee_count = 0

while True:
    command = input()

    if command == "END":
        print(coffee_count)
        break

    if command.isupper():
        if command == "CODING" \
                or command == "DOG" \
                or command == "CAT" \
                or command == "MOVIE":
            coffee_count += 2
        else:
            continue
    elif command.islower():
        if command == "coding" \
                or command == "dog" \
                or command == "cat" \
                or command == "movie":
            coffee_count += 1
        else:
            continue
    else:
        continue

    if coffee_count > COFFEE_LIMIT:
        print("You need extra sleep")
        break
