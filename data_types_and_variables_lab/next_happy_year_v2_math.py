year = int(input())

while True:
    year += 1
    temp_year = year
    is_happy = True

    while temp_year > 0:
        digit = temp_year % 10
        temp_year = temp_year // 10
        remaining_digit = temp_year

        while remaining_digit > 0:
            chek_digit = remaining_digit % 10
            if chek_digit == digit:
                is_happy = False
                break
            remaining_digit = remaining_digit // 10

        if not is_happy:
            break

    if is_happy:
        print(year)
        break
