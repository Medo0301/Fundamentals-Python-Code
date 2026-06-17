sequence_of_integers = [int(x) for x in input().split()]
average_value = sum(sequence_of_integers) / len(sequence_of_integers)

top_5_num = []
for _ in range(5):
    max_num = max(sequence_of_integers)
    if max_num > average_value:
        top_5_num.append(max_num)
        sequence_of_integers.remove(max_num)
    else:
        break
if top_5_num:
    print(*top_5_num)
else:
    print("No")
