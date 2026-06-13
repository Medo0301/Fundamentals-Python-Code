version = list(map(int, input().split(".")))

version[-1] += 1
for idx in range(len(version) - 1, 0, -1):
    if version[idx] > 9:
        version[idx] = 0
        version[idx - 1] += 1

version = list(map(str, version))

print(".".join(version))
