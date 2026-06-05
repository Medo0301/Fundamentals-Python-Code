row_1 = input().split()
row_2 = input().split()
row_3 = input().split()

winning_combo =[[row_1[0], row_1[1], row_1[2]],
                [row_2[0], row_2[1], row_2[2]],
                [row_3[0], row_3[1], row_3[2]],
                [row_1[0], row_2[0], row_3[0]],
                [row_1[1], row_2[1], row_3[1]],
                [row_1[2], row_2[2], row_3[2]],
                [row_1[0], row_2[1], row_3[2]],
                [row_1[2], row_2[1], row_3[0]]]

for combo in winning_combo:
    if combo[0] == combo[1] == combo[2] == '1':
        print("First player won")
        break
    elif combo[0] == combo[1] == combo[2] == '2':
        print("Second player won")
        break
else:
    print("Draw!")
