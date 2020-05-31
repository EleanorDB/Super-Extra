# Ella 31st May - Pat


import random
print("\nA long time ago in a galaxy far, far away... "
      "\nIt is a period of civil war. The Rebellion continue their fight against the evil Galactic Empire."
      "\nYou, young Jedi, have been chosen to help the Rebellion in the Battle of Star Wars Top Trumps."
      "\n"
      "\nYou must use the Force to choose a Starship with strong credentials which can defeat that chosen by the Empire. "
      "\nThe Starships’ characteristics will be compared and the strongest Starship wins the battle." 
      "\n"
      "\nYou gain 2 points for defeating the Empire, 1 point for a draw and 0 points for losing. "
      "\nOnly after winning 10 points will you succeed in defeating the Empire and restoring peace to the Galaxy."
      "\nMay the Force be with You.")

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

import sys

#starship allocation
def run():
    run.counter += 1
    score_list = []
    allocation_choice = input(
        '\nRound {}: Would you like to choose your card or be allocated a random one? Type C to choose or R for random. '.format(run.counter))
    choice_1 = random_starship1()
    choice_2 = random_starship2()
    while allocation_choice not in ['C', 'c', 'R', 'r']:
        print('\nThis is an invalid choice. Please choose again. ')
        allocation_choice = input(
            '\nRound {}: Would you like to choose your card or be allocated a random one? Type C to choose or R for random. '.format(run.counter))
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
        print("\nYou have been allocated the following Starship: '{}'. ".format(choice_1['name']))
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
        chosen_statistic = input("\nWhich statistic will you choose, young Jedi, in your fight against the Empire? \nPlease enter 'Cost', 'Length', 'Crew', 'Passengers', 'Speed', or 'Cargo'. ")
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
        else:
            print('\nThis is an invalid choice. Please choose again. ')
            choice_statistic()

        print("\nThe Empire has been allocated the starship: '{}'. ".format(computer_ship['name']))

        # Deciding who wins and keeping track of score
        def battle_cards():
        #turning API results for user & Empire into integers
            my_parsed_stat = str("")
            my_stat_int = int(0)
            emp_parsed_stat = str("")
            emp_stat_int = int(0)

            for c in my_statistic:
                try:
                    int(c)
                except:
                    pass
                else:
                    my_parsed_stat += c

            if my_parsed_stat != "":
                my_stat_int = int(my_parsed_stat)

            for c in empire_statistic:
                try:
                    int(c)
                except:
                    pass
                else:
                    emp_parsed_stat += c

            if emp_parsed_stat != "":
                emp_stat_int = int(emp_parsed_stat)

            print("\nYour statistic scores {}, while the Empire's statistic scores {}. ".format(my_stat_int, emp_stat_int))

            if my_stat_int > emp_stat_int:
                score_list.append('1')
                score_list.append('1')
                points_to_win = 10 - len(score_list)
                print("\nYou have won this battle against the evil Galactic Empire. Your score is now {}. "
                      "\nYou must score {} more points to fully defeat the Empire. "
                      "\nThe battle must continue for peace to be restored to the Galaxy...".format(len(score_list),
                                                                                                    points_to_win))
            elif emp_stat_int > my_stat_int:
                print("\nYou have been defeated by the Empire."
                      "\nYour score remains {}. "
                      "\nBut do not lose hope, young Jedi. Your time will come to restore peace to the Galaxy. ".format(len(score_list)))

            elif my_stat_int == emp_stat_int:
                score_list.append('1')
                print("\nIt's a draw! Continue playing to restore peace to the Galaxy. "
                      "\nYour score is now {}.".format(len(score_list)))

            # score tally to see whether user defeated the Empire - after 10 wins

            if len(score_list) >= 10:
                print("\nCongratulations, young Jedi. You have helped the Rebellion to defeat the Galactic Empire. Peace and freedom can now be restored to the Galaxy.")
                score_list.clear()
                sys.exit('Mission complete.')
            # user choice whether to continue with game (and continue score tally to 10 wins) or end it there
            elif len(score_list) < 10:
                continue_choice = input("\nWould you like to continue in your fight against the Empire? Enter 'Yes' or 'No'. ")
                if continue_choice == 'Yes':
                    run()
                else:
                    score_list.clear()
                    print("\nWe are disappointed in you, young Jedi. You must be resilient to defeat the Empire. ")
                    sys.exit('Lost hope.')
        battle_cards()
    choice_statistic()

run.counter = 0
run()