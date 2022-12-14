""" Create a list with magician names. The function show_magicians() should show each magician name.
- Create a function make_great that modifies the magician list and add the Great for each one.
- Use a copy of magician_names to show their name with Great """

magician_names = ['harry houdini','david copperfield',
    'crys angel']
great_list = []

def show_magician(magician_names):
    for magician in magician_names:
        print("Hello, " + magician.title())

def make_great(magician_names):
    for magician in magician_names:
        great_list.append('Great ' + magician)

make_great(magician_names[:])
show_magician(great_list)
show_magician(magician_names)
