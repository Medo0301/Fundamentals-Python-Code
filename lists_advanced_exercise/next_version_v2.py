version = input().split(".")

str_version = "".join(version)

next_version = int(str_version) + 1

result = list(str(next_version))

print(".".join(result))
