team_A = list(range(1, 12))
team_B = list(range(1, 12))

cards = input().split()

for card in cards:
    if len(team_A) < 7 or len(team_B) < 7:
        break

    team, player = card.split("-")
    player = int(player)
    if team == "A" and player in team_A:
        team_A.remove(player)
    elif team == "B" and player in team_B:
        team_B.remove(player)

print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")

if len(team_A) < 7 or len(team_B) < 7:
    print("Game was terminated")
