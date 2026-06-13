numbers = list(map(int, input().split(", ")))
boundary = 0

while len(numbers) > 0:
    boundary += 10
    result = [numbers.pop(idx) for idx in range(len(numbers) - 1, -1, -1) if numbers[idx] <= boundary]
    print(f"Group of {boundary}'s: {result[::-1]}")

