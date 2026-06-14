n = int(input())
positive = []
negative = []

for _ in range(n):
    num = int(input())
    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)

print(positive)
print(negative)
print(f"Count of positives: {len(positive)}")
print(f"Sum of negatives: {sum(negative)}")
