SAND = "sand"
WATER = "water"
FISH = "fish"
SUN = "sun"

text = input().lower()

counter = text.count(SAND) + text.count(WATER) \
          + text.count(FISH) + text.count(SUN)

print(counter)
