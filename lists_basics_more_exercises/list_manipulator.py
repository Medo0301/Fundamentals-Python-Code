list_of_numbers = [int(x) for x in input().split()]

while True:
    command = input()
    if command == "end":
        print(list_of_numbers)
        break
    elif "exchange" in command:
        index = int(command.split()[1])
        if 0 <= index < len(list_of_numbers):
            pass
        else:
            print("Invalid index")
    elif "max" in command:
        pass
    elif "min" in command:
        pass
    elif "first" in command:
        pass
    elif "last" in command:
        pass

