to_do_list = [""] * 10

while True:
    to_do = input().split("-")
    if to_do[0] == "End":
        break

    priority = int(to_do[0]) - 1
    to_do_list[priority] = to_do[1]

final_to_do = [todo for todo in to_do_list if todo != ""]
print(final_to_do)
