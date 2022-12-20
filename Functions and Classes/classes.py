### My first contact with Object Oriented Programming ###

""" In OOP, we write classes that represents entities and real world situations, them we create objects based on that classes. 
When we write a class, we define the general behavior that each category of objects can have.

When we create individual objects from a class, each object will have the general behavior by default. So we can give each object 
the desired attributes.

Creating an object from a class is known as instantiation, and we can work with instances of a class."""

# Defining and using a class

""" We will begin by creating a simple class named dog"""

class Dog():
    """ Creating a simple dog"""
    """ Initialize the name and age attributes"""
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    """ Simulates a dog sitting to respond a command"""    
    def sit(self):
        print(self.name.title() + " is now sitting.")
    """ Simulates a dog rolling to respond a command"""
    def roll_over(self):
        print(self.name.title() + " rolled over")
    
# The __init__() method:
""" A function that belongs to a class is a method. The only difference between functions and methods is the way we call them.
The __init__ is a special method that Python executes automatically each time we create a new instance based on the Dog class.
We defined the __init__ method to have three parameters: self, name and age. The self parameter is required when defining a 
method and must be the first one before any other parameters. All method calls will pass the self argument, it's a reference 
to the own instance, it gives access to each attribute and methods from the class to the individual instance."""

# Let's create one instance that represents a real dog:
my_dog = Dog('faraday',7,'male')

print("My dog name is " + my_dog.name.title() + ' and it is ' +
my_dog.sex + '.')
print("It is " + str(my_dog.age) + " years old.")

# Calling methods:
my_dog.sit()
my_dog.roll_over()

# Defining a new instance of.
your_dog = Dog('jullie',6,'female')

print("Your dog name is " + your_dog.name.title() + 
' and it is ' + your_dog.sex + '.')
print("It is " + str(my_dog.age) + " years old.")
your_dog.sit()

# Defining a new class Restaurant:

class Restaurant():
    """ Creating a restaurant class """
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    """ Creating a method to describe the restaurant """
    def describe_restaurant(self):
        print("Welcome to " + self.restaurant_name.title() +
        ". Here will you find the best of " + self.cuisine_type.title() + " cuisine!")
    def open(self):
        print(self.restaurant_name.title() + ' is now open!')
    def closed(self):
        print(self.restaurant_name.title() + ' is now closed!')

restaurant1 = Restaurant('naya palace','indian')
restaurant1.describe_restaurant()
restaurant1.open()

restaurant2 = Restaurant('shoney shouku','japanese')
restaurant2.describe_restaurant()
restaurant2.closed()

restaurant3 = Restaurant('tutto benne','italian')
restaurant3.describe_restaurant()
restaurant3.open()

# Working with classes:
# Let's create a class that represents a band:

class Band():
    """ A simple try to create a band"""
    def __init__(self,name,genre,year,most_successfull):
        self.name = name
        self.genre = genre
        self.year = year
        self.most_successfull = most_successfull
    """ Simple description of the band """
    def describe_band(self):
        print(self.name.title() + ' was formed in ' + str(self.year) 
        + '. Their main genre was ' + self.genre.title())
    """ Most successfull album """
    def successfull_album(self):
        print("Their most successfull album was " + self.most_successfull.title())
    
band1 = Band('the beatles','rock',1960,'sgt. peppers lonely hearts club band')
band2 = Band('pink floyd','rock',1965,'the dark side of the moon')

# Using the instances
band1.describe_band()
band1.successfull_album()

band2.describe_band()
band2.successfull_album()

# Default value to an attribute:
""" Each attribute from a class requires an inicial value, even if it's zero or an empty string. In some cases, we can specify this init value into the __init__ method. If it's done by an attribute, we don't need to include a parameter to it."""

# Continuing with our Band class, let's add one more info:
# Country = England to make England as the default country:
class Band():
    """ A simple try to create a band"""
    def __init__(self,name,genre,year,most_successfull):
        self.name = name
        self.genre = genre
        self.year = year
        self.most_successfull = most_successfull
        self.country = 'england'
    """ Simple description of the band """
    def describe_band(self):
        print(self.name.title() + ' was formed in ' + str(self.year) 
        + '. Their main genre was ' + self.genre.title())
    """ Most successfull album """
    def successfull_album(self):
        print("Their most successfull album was " + self.most_successfull.title())
    def country_origin(self):
        print("The band was formed in " + self.country.title())

band3 = Band('the beatles','rock',1960,'sgt. peppers lonely hearts club band')
band4 = Band('pink floyd','rock',1965,'the dark side of the moon')

# Creating a new band to change the default attribute country
band5 = Band('metallica','metal',1981,'metallica')
band5.country = 'united states'

# Using the instances
band3.describe_band()
band3.successfull_album()
band3.country_origin()

band4.describe_band()
band4.successfull_album()
band4.country_origin()

band5.describe_band()
band5.successfull_album()
band5.country_origin()

# Using a method to modify an attribute value:

# Page 208