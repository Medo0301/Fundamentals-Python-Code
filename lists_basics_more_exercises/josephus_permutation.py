start_list = [int(x) for x in input().split()]
num = int(input())
executed_list = []
executor = 0

while len(start_list) > 0:
    executor += (num - 1)
    if executor >= len(start_list):
        executor = executor % len(start_list)
    count_out = start_list.pop(executor)
    executed_list.append(count_out)

formatted_output = ",".join([str(x) for x in executed_list])
print(f"[{formatted_output}]")
