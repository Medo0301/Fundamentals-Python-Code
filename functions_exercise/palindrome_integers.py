def chek_for_palindrome_integer(list_of_int: list):
    for num in list_of_int:
        num = str(num)
        if num == num[::-1]:
            print(True)
        else:
            print(False)


list_numbers = [int(x) for x in input().split(", ")]

chek_for_palindrome_integer(list_numbers)
