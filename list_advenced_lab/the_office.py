def multiply_element_with_factor(elements: list, the_factor: int):
    return list(map(lambda x: x * the_factor, elements))


def happy_or_not_employees(employees: list, the_factor: int):
    multiply_happiness = multiply_element_with_factor(employees, the_factor)
    average_happiness = sum(multiply_happiness) / len(multiply_happiness)
    happy_count = sum(1 for num in multiply_happiness if num >= average_happiness)
    happy = "happy" if happy_count >= len(multiply_happiness) / 2 else "not happy"
    return f"Score: {happy_count}/{len(multiply_happiness)}. Employees are {happy}!"


employees_happiness = list(map(int, input().split()))
factor = int(input())
result = happy_or_not_employees(employees_happiness, factor)
print(result)

