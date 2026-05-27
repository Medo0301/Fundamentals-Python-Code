num = int(input())

for i in range(1, num + 1):
    for x in range(1, i + 1):
        print("*", end='')
    print()

for i in range(num - 1, 0, -1):
    for x in range(i, 0, -1):
        print("*", end='')
    print()
