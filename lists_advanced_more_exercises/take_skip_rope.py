hidden_message = list(input())
digit_list = [hidden_message.pop(idx) for idx in range(len(hidden_message) -1, -1, -1) if hidden_message[idx].isdigit()]
digit_list.reverse()
current_string = "".join(hidden_message)

take_list = [int(digit_list[idx]) for idx in range(len(digit_list)) if idx % 2 == 0]
skip_list = [int(digit_list[idx]) for idx in range(len(digit_list)) if idx % 2 != 0]

final_string = ""
start_take = 0
for idx in range(len(take_list)):
    end_take = start_take + take_list[idx]
    final_string += current_string[start_take:end_take]
    start_take += take_list[idx]
    start_take += skip_list[idx]

print(final_string)
