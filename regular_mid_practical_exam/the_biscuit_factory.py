from math import floor

MONTH = 30

biscuits_per_worker = int(input())
workers = int(input())
competitor_cookies_per_month = int(input())
total_biscuits_per_day = biscuits_per_worker * workers
total_production = 0

for day in range(1, MONTH + 1):
    if day % 3 == 0:
        total_production += floor(total_biscuits_per_day * 0.75)
    else:
        total_production += floor(total_biscuits_per_day)

print(f"You have produced {total_production} biscuits for the past month.")
the_difference = abs(total_production - competitor_cookies_per_month)
if total_production > competitor_cookies_per_month:
    print(f"You produce {the_difference / competitor_cookies_per_month * 100:.2f} percent more biscuits.")
else:
    print(f"You produce {the_difference / competitor_cookies_per_month * 100:.2f} percent less biscuits.")
