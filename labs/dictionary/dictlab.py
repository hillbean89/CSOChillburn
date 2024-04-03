"""
    CS110 Lab
    Dictionary Lab

    Updated By: Colin Hillburn

    CSCI 110
    Date: 4/02/2024

    Working with Python dictionary (dict) data structure.
"""
import os

# create a mapping of state names to their codes using a dictionary
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI',
    'Nebraska': 'NE',
    'Colorado': 'Co',
    'Wyoming': 'WY',
    'Idaho': 'Id',
    'Montatn':'MT'}

# create a mapping of states to their capital state using a dictionary
capitalCity = {
    'CA': 'Sacramento',
    'MI': 'Lansing',
    'FL': 'Tallahassee',
    'NY': 'Buffalo',
    'OR': 'Salem',
    'NE': 'Lincoln',
    'Co': 'Golden',
    'WY': 'Cheyenne',
    'Id': 'Boise',
    'MT': 'Helena'}

# add some more entires to capitalCity dictionary
capitalCity['NY'] = 'Albany'
capitalCity['OR'] = 'Salem'
capitalCity['NE'] = 'Lincoln'
capitalCity['Co'] = 'Denver'
capitalCity['WY'] = 'Cheyenne'
capitalCity['Id'] = 'Boise'
capitalCity['MT'] = 'Helena'
# FIXME4: Add rest of the states’ capital cities to capitalCity dictionary


def menu():
    print("""
            Enter one of the menu options:
            [1] Find US state's code given its name
            [2] Find US state's capital given its code
            [3] Find US state's capital given its name
            [4] Exit the program
        """)


def main():
    while True:
        # clear screen
        os.system('clear')
        # print menu
        menu()
        # get menu option
        option = input()
        if option == '4':
            print('SEE YOU AGAIN... GOOD BYE!')
            break

        if option == '1':
            state = input('Enter a US state name: ')
            if state in states:  # check if state is in states dict
                print('Code for {} is {}.'.format(state, states[state]))
            else:
                print("Sorry! The US state name '{}' NOT found!".format(state))
        elif option == '2':
            code=input('Enter a states code')
            if code in capitalCity:
                print('Capital for {} is {}'.format(code,capitalCity[code]))
            else:
                print("Sorry! The US state code '{}'NOT found!'".format(states))
            # FIXME5 - complete menu option 2#fixed

        elif option=='3':
            Place=input('Enter a state')
            retval= states.get(Place)
        if retval in capitalCity:
            
            print('the capital of colorado is {}'.format(capitalCity[retval]))
        else:
            print('sorry but you suck')
            

            



        # FIXME6 - complete menu option 3 FIXED

        # FIXME7 - handle the case where user enters invalid menu option
        print('Enter to continue...')
        
        input()


if __name__ == "__main__":
    main()