""" In this program, we will write a simple pool to ask why people like programming"""

pool_list = 'texts\pool_results.txt'

with open(pool_list, 'a') as pool:
    print("Welcome to DataStruct Pool\n")
    print("Please inform your name, if you like programming or not and tell us why." 
    + "Enter exit any time to leave:\n")
    guest_name = input("Please inform us your name: ")
    while guest_name != 'exit':
        pool.write('Name: ' + guest_name.title() + '\n')
        yes_or_no = input("Do you like programming? Yes or Not: ")
        pool.write('Do you like it: ' + yes_or_no.title() + '\n')
        reason = input("Could you tell us why: ")
        pool.write('Answer: ' + reason + '\n\n')
        pool.write('------------------------------------------')
        guest_name = input("Please inform us your name: ")
