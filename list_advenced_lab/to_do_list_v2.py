to_do_list = []

while True:
    to_do = input().split("-")
    if to_do[0] == "End":
        break

    to_do[0] = int(to_do[0])
    to_do_list.append(to_do)

to_do_list.sort()
result = [todo[1] for todo in to_do_list]
print(result)
