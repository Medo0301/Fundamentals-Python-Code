LITTLE_A_IN_ASCII = 97

num = int(input())

for first in range(num):
    for second in range(num):
        for third in range(num):
            print(f"{chr(LITTLE_A_IN_ASCII + first)}"
                  f"{chr(LITTLE_A_IN_ASCII + second)}"
                  f"{chr(LITTLE_A_IN_ASCII + third)}")
