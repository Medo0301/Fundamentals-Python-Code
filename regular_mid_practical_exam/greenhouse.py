def uproot(crops_line: list, crop_for_uproot):
    crops_line.remove(crop_for_uproot)


def plant(crops_line: list, new_crop: str):
    crops_line.insert(0, new_crop)


def transplant(crops_line: list, crop_for_transplant: str):
    uproot(crops_line, crop_for_transplant)
    crops_line.append(crop_for_transplant)


def replace(crops_line: list, first_crop_idx: int, second_crop_idx: int):
    crops_line[first_crop_idx], crops_line[second_crop_idx] = crops_line[second_crop_idx], crops_line[first_crop_idx]


crops = input().split(" & ")

while True:
    command = input()
    if command == "Collect!":
        print(" | ".join(crops))
        break
    command_parts = command.split()
    action = command_parts[0]
    crop = ""
    if action != "Replace":
        crop = command_parts[1]

    if action == "Plant" and crop not in crops:
        plant(crops, crop)
    elif action == "Transplant" and crop in crops:
        transplant(crops, crop)
    elif action == "Replace":
        first_crop_index = int(command_parts[1])
        second_crop_index = int(command_parts[2])
        if first_crop_index in range(len(crops)) and second_crop_index in range(len(crops)):
            replace(crops, first_crop_index, second_crop_index)
    elif action == "Uproot" and crop in crops:
        uproot(crops, crop)
