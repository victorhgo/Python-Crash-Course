""" Write the name of guests into guests.txt"""

guest = 'texts\guest.txt'

with open(guest, 'w') as guest_list:
    guest_name = input("What's the name of the guest?\n")
    guest_list.write(guest_name)