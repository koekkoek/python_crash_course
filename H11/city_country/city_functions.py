def city_country(city: str, country: str, population="") -> str:
    if population:
        return f"{city}, {country} - population {population}"

    return f"{city}, {country}"
