zeros_back = [int(x) for x in input().split(", ")]

for num in zeros_back:
    if num == 0:
        zeros_back.remove(num)
        zeros_back.append(num)

print(zeros_back)
