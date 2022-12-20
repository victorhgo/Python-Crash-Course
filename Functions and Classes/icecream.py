# This module file will contain the make ice cream function:

def make_icecreams(flavour,*toppings):
    print(" Making a(n) " + flavour.title() + 
    ' ice cream with the following toppings: ')
    for topping in toppings:
        print("- " + topping)