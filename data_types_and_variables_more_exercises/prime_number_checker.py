num = int(input())
is_prime = True

for n in range(2, num // 2 + 1):
    if num % n == 0:
        is_prime = False
        break

print(is_prime)