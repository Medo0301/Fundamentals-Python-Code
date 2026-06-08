# Check if the given number is even

def is_even(number):
    return number % 2 == 0


def its_perfect_number(number: int):
    # Optimization: Non-even numbers cannot be perfect, as their divisors
    # cannot sum up to the number itself. Avoids unnecessary loops.
    if is_even(number):
        divisor_sum = 0
        for divisor in range(1, number // 2 + 1):
            if number % divisor == 0:
                divisor_sum += divisor
        if divisor_sum == number:
            return "We have a perfect number!"
        else:
            return "It's not so perfect."
    else:
        return "It's not so perfect."


num = int(input())

result = its_perfect_number(num)
print(result)
