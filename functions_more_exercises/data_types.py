def process_data(data_type: str, value: str):
    if data_type == "int":
        return int(value) * 2
    elif data_type == "real":
        return f"{(float(value) * 1.5):.2f}"
    return f"${value}$"


the_type = input()
the_value = input()

result = process_data(the_type, the_value)
print(result)