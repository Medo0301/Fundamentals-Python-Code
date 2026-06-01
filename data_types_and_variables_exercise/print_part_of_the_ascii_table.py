start = int(input())
final = int(input())

for idx in range(start, final + 1):
    if idx == final:
        print(chr(idx))
    else:
        print(chr(idx), end=" ")
