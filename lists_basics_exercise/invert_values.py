list_number = input().split()

for idx in range(len(list_number)):
    list_number[idx] = int(list_number[idx]) * -1

print(list_number)
