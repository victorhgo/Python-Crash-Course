# Vehicle Rental Services - Write a program that allows the user to enter which
# vehicle he wants to rent.

# Available Vehicle Categories
cars_models = ('suv', 'sedan', 'compact', 'sport')

# Available Brands and Models
cars_suv = {'mitsubishi':'asx','honda':'hrv','volvo':'xc90'}
cars_sedan = {'honda':'civic','toyota':'corola','audi':'a7'}
cars_compact = {
    'mercedes':'class a','mercedes':'smart','fiat':'500'}
cars_sport = {'audi':'r8','chevy':'camaro','toyota':'supra'}

print(
    "Welcome to Yamada Rental services. We offer the following rent options:")
print('\n\tSUV\tSedan\tCompact\tSport')

option = input('What would you like to choose?: ')

if option.lower() == 'suv':
    for brand,model in cars_suv.items():
        print(
            'You can rent a ' + brand.title() + 
            ' ' + model.title() + '!')
if option.lower() == 'sedan':
    for brand,model in cars_sedan.items():
        print(
            'You can rent a ' + brand.title() + 
            ' ' + model.title() + '!')
if option.lower() == 'compact':                
    for brand,model in cars_compact.items():
        print(
            'You can rent a ' + brand.title() + 
            ' ' + model.title() + '!')
if option.lower() == 'sport':        
    for brand,model in cars_sport.items():
        print(
            'You can rent a ' + brand.title() + 
            ' ' + model.title() + '!')
