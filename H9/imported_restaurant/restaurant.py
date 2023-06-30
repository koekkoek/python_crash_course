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


class IceCreamStand(Restaurant):
    """A child class representing an Ice Cream Stand."""

    def __init__(self, restaurant_name, flavor):
        super().__init__(restaurant_name, "Ice Cream Stand")
        self.flavors = flavor

    def display_flavors(self):
        """Show wich flavors are available."""
        print(f"\n{self.restaurant_name} offers you the following flavor(s):")
        for flavor in self.flavors:
            print(f"- {flavor}")
