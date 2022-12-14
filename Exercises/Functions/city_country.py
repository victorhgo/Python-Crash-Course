# City Country:

def city_country(city_name, country_name):
    full_name = city_name + ', ' + country_name
    return full_name.title()

counter = 0
while counter < 3:
    city_name = input("\nEnter the city name: ")
    country_name = input("\nEnter the country name: ")
    counter += counter
    print(city_country(city_name,country_name))