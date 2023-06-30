class Restaurant:
    """A class representing a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"De naam van het restaurant: {self.restaurant_name}")
        print(f"De keuken van het restaurant: {self.cuisine_type}")

    def open_restaurant(self):
        print("Het restaurant is geopend.")


restaurant = Restaurant("Koeien en Kaas", "Hollands")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type, "\n")
restaurant.describe_restaurant()
restaurant.open_restaurant()
