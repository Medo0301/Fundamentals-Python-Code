def tribonacci_sequence(number: int):
    tribonacci_numbers = ['1']
    num_1 = 1
    num_2 = 0
    num_3 = 0
    for _ in range(number - 1):
        current_num = num_1 + num_2 + num_3
        tribonacci_numbers.append(str(current_num))
        num_3 = num_2
        num_2 = num_1
        num_1 = current_num

    return tribonacci_numbers


num = int(input())

result = tribonacci_sequence(num)

print(" ".join(result))