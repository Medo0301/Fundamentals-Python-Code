AVERAGE_DAYS_IN_YEAR = 365.2422
YEARS_IN_ONE_CENTURIES = 100
HOURS_IN_DAY = 24
MINUTES_IN_HOUR = 60

centuries = int(input())
years = centuries * YEARS_IN_ONE_CENTURIES
days = int(years * AVERAGE_DAYS_IN_YEAR)
hours = days * HOURS_IN_DAY
minutes = hours * MINUTES_IN_HOUR

print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")
