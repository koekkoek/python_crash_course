class Restaurant:
    """A class representing a restaurant."""

    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"De naam van het restaurant: {self.restaurant_name}")
        print(f"De keuken van het restaurant: {self.cuisine_type}")

    def open_restaurant(self):
        print("Het restaurant is geopend.")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number


# Maken instance
restaurant = Restaurant("Koeien en kaas", "Hollands", 100)

# Show numbers served
print(restaurant.number_served)

# Change numbers served and print new value
restaurant.number_served = 200
print(restaurant.number_served)

# Change numbers served with function and print it
restaurant.set_number_served(1500)
print(restaurant.number_served)

# Increment numbers served with function and print result
restaurant.increment_number_served(50)
print(restaurant.number_served)
