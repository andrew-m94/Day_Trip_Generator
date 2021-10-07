# Andrew Morales
from random import randrange

def pick_random(event):
    
    size = len(event)
    choice = randrange(0,size - 1)
    
    return event[choice]

def pick_option(options_list):
    
    user_answer = 'N'

    while user_answer == 'N':
        list_choice = pick_random(options_list)
        print('\n' + list_choice)

        if 'New York, NY' in options_list:
            which_list = 'destination'

        elif 'Hibachi' in options_list:
            which_list = 'food'

        elif 'Bus' in options_list:
            which_list = 'transportation'

        elif 'go shopping' in options_list:
            which_list = 'entertainment'
        
        user_answer = input(f'Is this {which_list} ok? Y/N: ').upper()
    
    return list_choice

def full_trip_print(destination,restaurant,transportation,entertainment):
    
    print(f'\nGreat! Your day trip will take place in {destination}.\nWhile you are there you will {entertainment}!\
\nAfter, you will be treated to some delicious {restaurant} for lunch.\nYou will move locations by way of \
{transportation}.\n')

def full_trip_confirm():

    user_input = input('Do you wish to confirm? Y/N ').upper()

    if user_input == 'N':
        run_program()
    
    else:
        print('\nEnjoy!')

def run_program():

    destinations = ['New York, NY', 'Los Angeles, CA', 'Houston, TX', 'Seattle, WA', 'Denver, CO']
    restaurants = ['Hibachi', 'Mcdonalds', 'Pasta', 'Steak,' 'Seafood']
    transportation = ['Bus', 'Taxi', 'Uber', 'Bicycle', 'Horse and Carriage']
    entertainment = ['go shopping', 'see a show', 'visit an amusement Park', 'visit the zoo', 'take a city Tour']

    final_destination = pick_option(destinations)
    final_restaurant = pick_option(restaurants)
    final_transportation = pick_option(transportation)
    final_entertainment = pick_option(entertainment)

    full_trip_print(final_destination, final_restaurant, final_transportation, final_entertainment)
    full_trip_confirm()

run_program()