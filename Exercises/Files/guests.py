""" Now we will create a guest list as guest_book.txt"""

guest_list = 'texts\guest_list.txt'

with open(guest_list, 'w') as guests:
    guest = input("What the guest name? Enter quit to exit: ")
    guests.write("\t -- People I'd like to invite --\n")
    while guest != 'quit':
        guests.write(guest + '\n')
        guest = input("What the guest name? Enter quit to exit: ")