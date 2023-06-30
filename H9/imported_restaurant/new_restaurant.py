from restaurant import Restaurant

restaurant = Restaurant("Koeien en kaas", "Hollands")
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(200)
print(restaurant.number_served)
