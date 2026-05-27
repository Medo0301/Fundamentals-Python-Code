number = int(input())

str_num = str(number)
largest_num_str = ""

for digit in range(9, -1, -1):
    digit_char = str(digit)
    count = str_num.count(digit_char)
    largest_num_str += digit_char * count

print(largest_num_str)