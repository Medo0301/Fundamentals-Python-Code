from math import floor


def distance_score(x: float, y: float):
    return x ** 2 + y ** 2


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

first_distance = distance_score(x1, y1)
second_distance = distance_score(x2, y2)

if first_distance <= second_distance:
    print(f"({floor(x1)}, {floor(y1)})")
else:
    print(f"({floor(x2)}, {floor(y2)})")
