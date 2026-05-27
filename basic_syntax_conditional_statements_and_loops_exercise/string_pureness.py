number_of_strings = int(input())

for _ in range(number_of_strings):
    text = input()

    if "," in text or "." in text or "_" in text:
        print(f"{text} is not pure!")
    else:
        print(f"{text} is pure.")
