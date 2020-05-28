import random

print('\nA long time ago in a galaxy far, far away... '
      '\nIt is a period of civil war. The Rebellion continue their fight against the evil Galactic Empire.'
      '\nYou, young Jedi, have been chosen to help the Rebellion in the Battle of Star Wars Top Trumps.'
      '\nIn some rounds, you must use the Force to choose the starship’s strongest characteristic, which will be compared to the Galactic Empire’s allocated card.'
      '\nIn other rounds, the Galactic Empire will have the upper hand and will choose the statistic to be compared.'
      '\nThe side with the highest statistic wins.'
      '\nYour score will be recorded. Only after choosing 10 winning cards will you succeed in defeating the Empire.'
      '\nMay the Force be with You.')

import requests

starship_list = [2, 3, 5, 9, 10, 11, 12, 13, 15, 17]

starship_sample = random.sample(starship_list, 3)

# 2 random starships chosen for user & stats returned
def random_starship1():
    starship_number1 = starship_sample[0]
    url = 'https://swapi.dev/api/starships/{}/'.format(starship_number1)
    response = requests.get(url)
    starship1 = response.json()
    return{
        'name':starship1['name'],
        'value':starship1['cost_in_credits'],
        'length':starship1['length'],
        'max atmosphering speed':starship1['max_atmosphering_speed'],
        'max sublight speed (MGLT)':starship1['MGLT'],
        'number of crew members':starship1['crew'],
        'passengers':starship1['passengers'],
        'cargo capacity':starship1['cargo_capacity'],
        'hyperdrive rating':starship1['hyperdrive_rating'],
    }

def random_starship2():
    starship_number2 = starship_sample[1]
    url = 'https://swapi.dev/api/starships/{}/'.format(starship_number2)
    response = requests.get(url)
    starship2 = response.json()
    return{
        'name':starship2['name'],
        'value':starship2['cost_in_credits'],
        'length':starship2['length'],
        'max atmosphering speed':starship2['max_atmosphering_speed'],
        'max sublight speed (MGLT)':starship2['MGLT'],
        'number of crew members':starship2['crew'],
        'passengers':starship2['passengers'],
        'cargo capacity':starship2['cargo_capacity'],
        'hyperdrive rating':starship2['hyperdrive_rating'],
    }

# 1 random starship chosen for computer

def random_starship3():
    starship_number3 = starship_sample[2]
    url = 'https://swapi.dev/api/starships/{}/'.format(starship_number3)
    response = requests.get(url)
    starship3 = response.json()
    return {
        'name': starship3['name'],
        'value': starship3['cost_in_credits'],
        'length': starship3['length'],
        'max atmosphering speed': starship3['max_atmosphering_speed'],
        'max sublight speed (MGLT)': starship3['MGLT'],
        'number of crew members': starship3['crew'],
        'passengers': starship3['passengers'],
        'cargo capacity': starship3['cargo_capacity'],
        'hyperdrive rating': starship3['hyperdrive_rating'],
    }

computer_ship = random_starship3()


#starship allocation
def run():
    round_count = 0

    allocation_choice = input(
        '\nRound {}: Would you like to choose your card or be allocated a random one? Type C to choose or R for random. '.format(
            round_count + 1))

    choice_1 = random_starship1()
    choice_2 = random_starship2()

    while allocation_choice not in ['C', 'c', 'R', 'r']:
        print('\nThis is an invalid choice. Please choose again. ')
        allocation_choice = input(
            '\nRound {}: Would you like to choose your card or be allocated a random one? Type C to choose or R for random. '.format(
                round_count + 1))
    if allocation_choice == 'C':
        chosen_ship = input("\nYou have a choice between Starship 1: '{}' or Starship 2: '{}'. Please type 1 or 2 to make your choice. ".format(choice_1['name'], choice_2['name']))
        if chosen_ship == '1':
            my_ship = choice_1
        elif chosen_ship == '2':
            my_ship = choice_2

        print("\nYou have chosen '{}'. ".format(my_ship['name']))

    elif allocation_choice == 'c':
        chosen_ship = input("\nYou have a choice between Starship 1: '{}' or Starship 2: '{}'. Please type 1 or 2 to make your choice".format(choice_1['name'], choice_2['name']))
        if chosen_ship == '1':
            my_ship = choice_1
        elif chosen_ship == '2':
            my_ship = choice_2

        print("\nYou have chosen '{}'".format(my_ship['name']))

    elif allocation_choice == 'R' or 'r':
        my_ship = choice_1
        print("\nYou have been allocated the following Starship: '{}'".format(choice_1['name']))

    # Present starship statistics
    print("\nThis starship's statistics are: "
              "\nCost (Galactic Credits): {} "
              "\nLength (m): {} "
              "\nCrew needed: {} "
              "\nPassengers allowed: {} "
              "\nMaximum Atmosphering Speed: {} "
              "\nCargo capacity (kg): {}".format(my_ship['value'], my_ship['length'],
                                                 my_ship['number of crew members'],
                                                 my_ship['passengers'],
                                                 my_ship['max atmosphering speed'],
                                                 my_ship['cargo capacity']))

    # User chooses statistic to play
    def choice_statistic():
        chosen_statistic = input(
            "\nWhich statistic will you choose, young Jedi, in your fight against the Empire? \nPlease enter 'Cost', 'Length', 'Crew', 'Passengers', 'Speed', or 'Cargo'. ")

        print("\nThe Empire has been allocated the starship: '{}'. ".format(computer_ship['name']))

        if chosen_statistic == 'Cost':
            my_statistic = my_ship['value']
            empire_statistic = computer_ship['value']
        elif chosen_statistic == 'Length':
            my_statistic = my_ship['length']
            empire_statistic = computer_ship['length']
        elif chosen_statistic == 'Crew':
            my_statistic = my_ship['number of crew members']
            empire_statistic = computer_ship['number of crew members']
        elif chosen_statistic == 'Passengers':
            my_statistic = my_ship['passengers']
            empire_statistic = computer_ship['passengers']
        elif chosen_statistic == 'Speed':
            my_statistic = my_ship['max atmosphering speed']
            empire_statistic = computer_ship['max atmosphering speed']
        elif chosen_statistic == 'Cargo':
            my_statistic = my_ship['cargo capacity']
            empire_statistic = computer_ship['cargo capacity']


        print("\nYour statistic scores {}, while the Empire's statistic scores {}. ".format(my_statistic, empire_statistic))

        # Deciding who wins and keeping track of score
        def battle_cards():
            score = 0
            if my_statistic > empire_statistic:
                print("\nYou have won your {} victory against the evil Galactic Empire."
                      "\nYour score is {}. "
                      "\nBut the battle must continue for peace to be restored to the galaxy...".format(round_count,
                                                                                                       score + 1))
            elif empire_statistic > my_statistic:
                print("\nYou have been defeated by the Empire."
                      "\nYour score remains {}. "
                      "\nBut do not lose hope, young Jedi. Your time will come to restore peace to the galaxy.".format(
                    score))
            else:
                print("\nIt's a draw! Continue playing to restore peace to the galaxy")

        battle_cards()

    choice_statistic()


run()

import sys

#score tally to see whether user defeated the Empire - after 10 wins
if score >= 10:
    print("Congratulations, young Jedi. After 10 victories in battle, you have helped the Rebellion to defeat the Galactic Empire. Peace and freedom can now be restored to the Galaxy.")
    sys.exit('Mission complete.')

#user choice whether to continue with game (and continue score tally to 10 wins) or end it there
elif score < 10:
    continue_choice = input("Would you like to continue in your fight against the Empire? Enter 'Yes' or 'No'. ")
    if continue_choice == 'Yes':
        run()
    else:
        print("We are disappointed in you, young Jedi. You must be resilient to defeat the Empire. ")
        sys.exit('Lost hope.')
