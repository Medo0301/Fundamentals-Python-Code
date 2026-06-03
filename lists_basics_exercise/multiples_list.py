factor = int(input())
count = int(input())
next_num = factor
multiples_list = []

for _ in range(count):
    multiples_list.append(next_num)
    next_num += factor
    
print(multiples_list)
