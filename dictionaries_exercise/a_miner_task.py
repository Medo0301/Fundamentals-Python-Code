resources = {}
command = input()
while command != "stop":
    current_resource = command
    quantity = int(input())
    if current_resource not in resources:
        resources[current_resource] = quantity
    else:
        resources[current_resource] += quantity

    command = input()

for resource in resources:
    print(f"{resource} -> {resources[resource]}")
