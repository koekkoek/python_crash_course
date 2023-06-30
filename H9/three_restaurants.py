class Restaurant:
    """A class representing a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\nDe naam van het restaurant: {self.restaurant_name}")
        print(f"De keuken van het restaurant: {self.cuisine_type}")

    def open_restaurant(self):
        print("Het restaurant is geopend.")


# Thee different instances from the class
restaurant1 = Restaurant("Koeien en Kaas", "Hollands")
restaurant2 = Restaurant("Saphori", "Italiaans")
restaurant3 = Restaurant("Al kalh", "Turks")

# Describe restaurants
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
