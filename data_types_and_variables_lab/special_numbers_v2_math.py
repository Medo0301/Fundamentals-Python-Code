FIRST_SPECIAL_NUM = 5
SECOND_SPECIAL_NUM = 7
THIRD_SPECIAL_NUM = 11

num = int(input())

for n in range(1, num + 1):
    digits_sum = 0
    is_special = False
    digits = n

    while digits > 0:
        digits_sum += digits % 10
        digits = digits // 10

    if digits_sum == FIRST_SPECIAL_NUM \
            or digits_sum == SECOND_SPECIAL_NUM \
            or digits_sum == THIRD_SPECIAL_NUM:
        is_special = True

    print(f"{n} -> {is_special}")