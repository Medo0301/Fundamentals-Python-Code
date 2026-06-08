def loading_bar(number: int):
    percent_count = number // 10
    dots_count = 10 - percent_count
    bar_visual = f"[{'%' * percent_count}{'.' * dots_count}]"
    if number != 10:
        return f"{number}% {bar_visual}", "Still loading..."
    else:
        return f"{number}% Complete!", bar_visual


num = int(input())
result1, result2 = loading_bar(num)

print(result1)
print(result2)
