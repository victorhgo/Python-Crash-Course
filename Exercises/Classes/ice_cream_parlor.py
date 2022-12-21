""" Write a class named IceCreamStand that inherits the Restaurant class. 
Add one attribute called flavours that stores a list of ice cream flavours. 
Write a method to show these flavours."""

class Restaurant():
    """ A simple way to describe a restaurant"""
    def __init__(self,restaurant_name,cuisine):
        self.restaurant_name = restaurant_name
        self.cuisine = cuisine
        self.status = 'open'
        self.number_served = 0
    """ Describe the restaurant """
    def describe_restaurant(self):
        print("Welcome to " + self.restaurant_name.title()
        + ". The best " + self.cuisine.title() + " food in town!")
    """ Describe if the restaurant is open or not"""
    def open_or_closed(self,restaurant_status):
        self.status = restaurant_status
        if restaurant_status == 'open':
            print(self.restaurant_name.title() + " is now open.")
        elif restaurant_status == 'closed':
            print(self.restaurant_name.title() + " is now closed!")
        else:
            print("Error, not found")
    """ How much people were already served"""
    def set_number_served(self,served):
        self.number_served = served
    def increment_number_served(self):
        self.number_served = self.number_served + 1
    def show_served(self):
        print("Today, we've already served", self.number_served, 'people')

""" Test the restaurant class."""
# new_restaurant = Restaurant('sukimiko','japanese')
# new_restaurant.describe_restaurant()
# new_restaurant.open_or_closed('closed')

""" Let's define our ice cream parlor as IceCreamStand class"""

class IceCreamStand(Restaurant):
    """ Init the IceCreamStand class with Restaurant class attributes and methods"""
    def __init__(self, restaurant_name,cuisine):
        super().__init__(restaurant_name, cuisine)
        self.flavours = ['vanilla','chocolate','strawberry','cream','passion fruit']
    """ Display each flavour served in a formatted way """    
    def show_flavours(self):
        print("We have the following flavours:")
        for flavour in self.flavours:
            print("\t-" + flavour.title())
    """ Rewriting the describe_restaurant method to display only ice cream"""
    def describe_restaurant(self):
        print("Welcome to " + self.restaurant_name.title()
        + ". The best " + self.cuisine.title() + " in town!")
    
ice_cream_parlor = IceCreamStand('summer dream','ice cream')
ice_cream_parlor.describe_restaurant()
ice_cream_parlor.show_flavours()

# End of the exercise