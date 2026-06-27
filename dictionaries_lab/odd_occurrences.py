elements = input().lower().split()

elements_dict = {}
for element in elements:
    if element not in elements_dict:
        elements_dict[element] = 1
    else:
        elements_dict[element] += 1

result = [element for element in elements_dict if elements_dict[element] % 2 != 0]

print(" ".join(result))
