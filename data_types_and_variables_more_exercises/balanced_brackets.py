n = int(input())
is_open_brackets = False

for _ in range(n):
    random_str = input()
    if random_str == "(" and is_open_brackets == False:
        is_open_brackets = True
    elif random_str == "(" and is_open_brackets == True:
        print("UNBALANCED")
        break
    elif random_str == ")" and is_open_brackets == True:
        is_open_brackets = False
    elif random_str == ")" and is_open_brackets == False:
        print("UNBALANCED")
        break
else:
    print("BALANCED")
