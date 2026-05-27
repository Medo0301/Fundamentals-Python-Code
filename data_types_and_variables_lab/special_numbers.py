FIRST_SPECIAL_NUM = 5
SECOND_SPECIAL_NUM = 7
THIRD_SPECIAL_NUM = 11

num = int(input())

for i in range(1, num + 1):
    is_special = False
    str_i = str(i)
    digit_sum = 0

    for digit in str_i:
        digit_sum += int(digit)

    if digit_sum == FIRST_SPECIAL_NUM \
            or digit_sum == SECOND_SPECIAL_NUM \
            or digit_sum == THIRD_SPECIAL_NUM:
        is_special = True

    print(f"{i} -> {is_special}")
