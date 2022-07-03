travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"],
    },
    {
        "country": "Germany",
        "visits": 2,
        "cities": ["Berlin", "Hamburg", "Stuttgart"],
    }
]


def add_new_city(country, visits, cities):
    new_country = {"country": country, "visits": visits, "cities": cities}
    travel_log.append(new_country)


add_new_city("russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
