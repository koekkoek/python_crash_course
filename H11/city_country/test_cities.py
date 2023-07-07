from city_functions import city_country


def test_city_country():
    alphen = city_country("Alphen aan den Rijn", "Nederland")
    assert alphen == "Alphen aan den Rijn, Nederland"


def test_city_country_population():
    bodegraven = city_country("Bodegraven", "Nederland", 35000)
    assert bodegraven == "Bodegraven, Nederland - population 35000"
