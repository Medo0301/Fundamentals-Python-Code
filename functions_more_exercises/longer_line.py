from math import floor, sqrt


def get_lime_length(x1: float, y1: float, x2: float, y2: float):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def distance_score(x: float, y: float):
    return x ** 2 + y ** 2


def get_ordered_points_string(x1: float, y1: float, x2: float, y2: float):
    if distance_score(x1, y1) <= distance_score(x2, y2):
        return f"({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})"
    return f"({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})"


first_x = float(input())
first_y = float(input())
second_x = float(input())
second_y = float(input())
third_x = float(input())
third_y = float(input())
forth_x = float(input())
forth_y = float(input())

first_line_length = get_lime_length(first_x, first_y, second_x, second_y)
second_line_length = get_lime_length(third_x, third_y, forth_x, forth_y)
result = ""
if first_line_length >= second_line_length:
    result = get_ordered_points_string(first_x, first_y, second_x, second_y)
else:
    result = get_ordered_points_string(third_x, third_y, forth_x, forth_y)

print(result)
