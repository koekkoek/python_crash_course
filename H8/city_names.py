def city_country(city, country):
    info = f"{city.title()}, {country.title()}"
    return info


print(city_country("alphen", "nederland"))
print(city_country("london", "england"))
print(city_country("berlin", "germany"))
