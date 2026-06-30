country = input().split(", ")
cities = input().split(", ")

date = zip(country, cities)
country_city_dict = {kay: value for (kay, value) in date}

for country in country_city_dict:
    print(f"{country} -> {country_city_dict[country]}")
    