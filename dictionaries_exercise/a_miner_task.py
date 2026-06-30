resources = {}
command = input()
while command != "stop":
    concurrent_resource = command
    quantity = int(input())
    if concurrent_resource not in resources:
        resources[concurrent_resource] = quantity
    else:
        resources[concurrent_resource] += quantity

    command = input()

for resource in resources:
    print(f"{resource} -> {resources[resource]}")
