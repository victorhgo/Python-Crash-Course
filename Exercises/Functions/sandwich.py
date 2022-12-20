# Write a function that receives a list of items that a person wants in a sandwich.

def build_sandwich(bread, *options):
    print('Your sandwich will be mounted on '
    + bread.title() + ' bread and will have:')
    for option in options:
        print("- " + option)

sandwich1 = build_sandwich('australian','ham','tomato','mayo','mustard','lettuce','cheddar')
sandwich2 = build_sandwich('pita','tuna','onions','cream cheese','black olives')
sandwich2 = build_sandwich('brioche','steak','arugula','barbecue sauce')