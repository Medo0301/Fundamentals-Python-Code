coins_list = input().split(", ")
count_beggars = int(input())

beggars_sums = [0] * count_beggars
beggar = 0

for coin in coins_list:
    coin = int(coin)
    beggars_sums[beggar] += coin
    beggar += 1
    if beggar == len(beggars_sums):
        beggar = 0

print(beggars_sums)
