#VERSION WHERE SCORE FINALLY WORKS!!!!!!

import random
import requests
import sys
from termcolor import colored

print(colored("\nA long time ago in a galaxy far, far away... ", 'yellow', attrs=['bold', 'underline']),
      colored("\nIt is a period of civil war. The Rebellion continue their fight against the evil Galactic Empire."
      "\nYou, young Jedi, have been chosen to help the Rebellion in the Battle of Star Wars Top Trumps."
      "\n"
      "\nYou must use the Force to choose a Starship with strong credentials which can defeat that chosen by the Empire. "
      "\nThe Starships’ characteristics will be compared and the strongest Starship wins the battle." 
      "\n"
      "\nYou gain", 'yellow'), colored("2 points for defeating the Empire, 1 point for a draw and 0 points for losing. ", 'red'),
      colored("\nOnly after winning", 'yellow'), colored("7 points", 'red'), colored("will you succeed in defeating the Empire and restoring peace to the Galaxy."
      "\nMay the Force be with You.", 'yellow'))

# 2 random starships chosen for user & stats returned
def random_starship1(starship_to_be_inserted):
    starship_number1 = starship_to_be_inserted[0]
    url = 'https://swapi.dev/api/starships/{}/'.format(starship_number1)
    response = requests.get(url)
    starship1 = response.json()
    return{
        'name': starship1['name'],
        'value': starship1['cost_in_credits'],
        'length': starship1['length'],
        'max atmosphering speed': starship1['max_atmosphering_speed'],
        'max sublight speed (MGLT)': starship1['MGLT'],
        'number of crew members': starship1['crew'],
        'passengers': starship1['passengers'],
        'cargo capacity': starship1['cargo_capacity'],
        'hyperdrive rating': starship1['hyperdrive_rating'],
    }

def random_starship2(starship_to_be_inserted):
    starship_number2 = starship_to_be_inserted[1]
    url = 'https://swapi.dev/api/starships/{}/'.format(starship_number2)
    response = requests.get(url)
    starship2 = response.json()
    return{
        'name': starship2['name'],
        'value': starship2['cost_in_credits'],
        'length': starship2['length'],
        'max atmosphering speed': starship2['max_atmosphering_speed'],
        'max sublight speed (MGLT)': starship2['MGLT'],
        'number of crew members': starship2['crew'],
        'passengers': starship2['passengers'],
        'cargo capacity': starship2['cargo_capacity'],
        'hyperdrive rating': starship2['hyperdrive_rating'],
    }

# 1 random starship chosen for computer
def random_starship3(starship_to_be_inserted):
    starship_number3 = starship_to_be_inserted[2]
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

#starship allocation
def run(total_score):
    run.counter += 1
    print(colored('\nRound {}: Would you like to choose your card or be allocated a random one?'.format(run.counter), 'blue'))
    allocation_choice = input(colored('Type C to choose or R for random. ', 'magenta'))

    starship_list = [2, 3, 5, 9, 10, 11, 12, 13, 15, 17]

    starship_sample = random.sample(starship_list, 3)

    choice_1 = random_starship1(starship_sample)
    choice_2 = random_starship2(starship_sample)
    computer_ship = random_starship3(starship_sample)

    while allocation_choice not in ['C', 'c', 'R', 'r']:
        print(colored('\nThis is an invalid choice. Please choose again. ', 'red'))
        print(colored('\nRound {}: Would you like to choose your card or be allocated a random one?'.format(run.counter), 'blue'))
        allocation_choice = input(colored(' Type C to choose or R for random. ', 'magenta'))

    if allocation_choice in ['C', 'c']:
        print(colored("\nYou have a choice between Starship 1: '{}' or Starship 2: '{}'.".format(choice_1['name'], choice_2['name']), 'blue'))
        chosen_ship = input(colored("Please type 1 or 2 to make your choice. ", 'magenta'))
        if chosen_ship == '1':
            my_ship = choice_1
        elif chosen_ship == '2':
            my_ship = choice_2
        print(colored("\nYou have chosen '{}'. ".format(my_ship['name']), 'green'))
    elif allocation_choice in ['R' or 'r']:
        my_ship = choice_1
        print(colored("\nYou have been allocated the following Starship: '{}'. ".format(choice_1['name']), 'green'))

    # Present starship statistics
    print(colored("\nThis starship's statistics are: ", 'yellow'),
              colored("\nCost (Galactic Credits): {} "
              "\nLength (m): {} "
              "\nCrew needed: {} "
              "\nPassengers allowed: {} "
              "\nMaximum Atmosphering Speed: {} "
              "\nCargo capacity (kg): {}".format(my_ship['value'], my_ship['length'],
                                                 my_ship['number of crew members'],
                                                 my_ship['passengers'],
                                                 my_ship['max atmosphering speed'],
                                                 my_ship['cargo capacity']), 'cyan'))

    # User chooses statistic to play
    def choice_statistic(total_score):
        print(colored("\nWhich statistic will you choose, young Jedi, in your fight against the Empire? ", 'blue'))
        chosen_statistic = input(colored("Please enter 'Cost', 'Length', 'Crew', 'Passengers', 'Speed', or 'Cargo'. ", 'magenta'))
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
            print(colored('\nThis is an invalid choice. Please choose again. ', 'red'))
            choice_statistic()

        print(colored("\nThe Empire has been allocated the starship: '{}'. ".format(computer_ship['name']), 'green'))

    # Deciding who wins and keeping track of score
        def battle_cards(total_score):
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

            print(colored("\nYour statistic scores {}, while the Empire's statistic scores {}. ".format(my_stat_int, emp_stat_int), 'cyan'))

            if my_stat_int > emp_stat_int:
                total_score += 2
                if total_score >= 7:
                    print(colored(
                        "\nCongratulations, young Jedi. You have helped the Rebellion to defeat the Galactic Empire. Peace and freedom can now be restored to the Galaxy.", 'magenta'))
                    sys.exit('Mission complete.')
                points_to_win = 7 - total_score
                print(colored("\nYou have won this battle against the evil Galactic Empire.", 'green'), colored("Your score is now {}. ".format(total_score), 'magenta'),
                      colored("\nYou must score {} more points to fully defeat the Empire. ".format(points_to_win), 'magenta'),
                      colored("\nThe battle must continue for peace to be restored to the Galaxy...", 'green'))

            elif emp_stat_int > my_stat_int:
                print(colored("\nYou have been defeated by the Empire.", 'red'),
                      colored("\nYour score remains {}. ".format(total_score), 'magenta'),
                      colored("\nBut do not lose hope, young Jedi. Your time will come to restore peace to the Galaxy. ", 'red'))

            elif my_stat_int == emp_stat_int:
                total_score += 1
                if total_score >= 7:
                    print(colored(
                        "\nCongratulations, young Jedi. You have helped the Rebellion to defeat the Galactic Empire. Peace and freedom can now be restored to the Galaxy.", 'magenta'))
                    sys.exit('Mission complete.')
                print(colored("\nIt's a draw! Continue playing to restore peace to the Galaxy. ", 'yellow'),
                      colored("\nYour score is now {}.".format(total_score), 'magenta'))

            while(True):
                print(colored("\nWould you like to continue in your fight against the Empire?", 'blue'))
                continue_choice = input(colored("Enter 'Yes' or 'No'. ", 'magenta'))
                if continue_choice in ['Yes', 'Y', 'y', 'Ye']:
                    run(total_score)
                    break
                else:
                    print(colored("\nWe are disappointed in you, young Jedi. You must be resilient to defeat the Empire. ", 'red'))
                    sys.exit('Lost hope.')

        battle_cards(total_score)
    choice_statistic(total_score)

run.counter = 0

total_score = 0
run(0)
