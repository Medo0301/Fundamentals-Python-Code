MONTH = 30
KG_TO_G = 1000
FOOD_FOR_A_DAY = 300

food = float(input()) * KG_TO_G
hay = float(input()) * KG_TO_G
cover = float(input()) * KG_TO_G
weight = float(input()) * KG_TO_G
cover_per_change = weight / 3

for day in range(1, MONTH + 1):
    food -= FOOD_FOR_A_DAY
    if day % 2 == 0:
        hay -= (food * 0.05)
    if day % 3 == 0:
        cover -= cover_per_change
    if food <= 0 or hay <= 0 or cover <= 0:
        print("Merry must go to the pet store!")
        break
else:
    print(f"Everything is fine! Puppy is happy! "
          f"Food: {food / 1000:.2f}, Hay: {hay / 1000:.2f}, Cover: {cover / 1000:.2f}.")
