#Ella Tues 26 May

import random

#tested opening and works
"""print('A long time ago in a galaxy far, far away... '
      '\nIt is a period of civil war. The Rebellion continue their fight against the evil Galactic Empire.'
      '\nYou, young Jedi, have been chosen to help the Rebellion in the Battle of Star Wars Top Trumps.'
      '\nIn some rounds, you must use the Force to choose the starship’s strongest characteristic, which will be compared to the Galactic Empire’s allocated card.'
      '\nIn other rounds, the Galactic Empire will have the upper hand and will choose the statistic to be compared.'
      '\nThe side with the highest statistic wins.'
      '\nYour score will be recorded. Only after choosing 10 winning cards will you succeed in defeating the Empire.'
      '\nIf you wish to flee the battle scene before the war is won, type: ‘I have lost hope.’'
      '\nMay the Force be with You.')
"""

import requests

starship_list = [2, 3, 5, 9, 10, 11, 12, 13, 15, 17]

starship_sample = random.sample(starship_list, 3)

#2 random starships chosen for user
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

#1 random starship chosen for computer
def random_starship3():
    starship_number3 = starship_sample[2]
    url = 'https://swapi.dev/api/starships/{}/'.format(starship_number3)
    response = requests.get(url)
    starship3 = response.json()
    return{
        'name':starship3['name'],
        'value':starship3['cost_in_credits'],
        'length':starship3['length'],
        'max atmosphering speed':starship3['max_atmosphering_speed'],
        'max sublight speed (MGLT)':starship3['MGLT'],
        'number of crew members':starship3['crew'],
        'passengers':starship3['passengers'],
        'cargo capacity':starship3['cargo_capacity'],
        'hyperdrive rating':starship3['hyperdrive_rating'],
    }

computer_ship = starship3

#starship allocation
def run():
    round_count = 0

    allocation_choice = input(
        'Round {}: Would you like to choose your card or be allocated a random one? Type C to choose or R for random. '.format(
            round_count + 1))

    choice_1 = random_starship1()
    choice_2 = random_starship2()

    while allocation_choice not in ['C', 'c', 'R', 'r']:
        print('This is an invalid choice. Please choose again')
        allocation_choice = input(
            'Round {}: Would you like to choose your card or be allocated a random one? Type C to choose or R for random. '.format(
                round_count + 1))
    if allocation_choice == 'C' or 'c':
        chosen_ship = input("You have a choice between Starship 1: '{}' or Starship 2: '{}'. Please type 1 or 2 to make your choice".format(choice_1['name'], choice_2['name']))
        if chosen_ship == '1':
              chosen_ship = choice_1
        elif chosen_ship == '2':
              chosen_ship = choice_2
        print("You have chosen {}".format(chosen_ship)
    elif allocation_choice == 'R' or 'r':
        print("You have been allocated the following Starship: '{}'".format(choice_1['name']))


run()

#present starship statistics
print("You have been allocated the following starship: "
      "\nName: {} ".format(chosen_ship['name']))
print("This starship's statistics are: "
      "\nCost (Galactic Credits): {} "
      "\nLength (m): {} "
      "\nCrew needed: {} "
      "\nPassengers allowed: {} "
      "\nMaximum Atmosphering Speed: {} "
      "\nCargo capacity (kg): {}".format(chosen_ship['cost in credits'], chosen_ship['length'], chosen_ship['crew'], chosen_ship['passengers'], chosen_ship['maximum atmosphering speed'], chosen_ship['cargo capacity']))

#user chooses statistic to play
def choice_statistic():
      chosen_statistic = input("Which statistic will you choose, young Jedi, in your fight against the Empire? Please enter 'Cost', 'Length', 'Crew', 'Passengers', 'Speed' or 'Cargo'. ")

      print("The Empire has been allocated {} starship".format(computer_ship['name']))

      if chosen_statistic == 'Cost':
            chosen_statistic = chosen_ship['cost in credits']
            empire_statistic = computer_ship['cost in credits']
            print("Your statistic scores {}, while the Empire's statistic scores {}".format(chosen_statistic, empire_statistic))
      elif chosen_statistic == 'Length':
            chosen_statistic = chosen_ship['length']
            empire_statistic = computer_ship['length']
            print("Your statistic scores {}, while the Empire's statistic scores {}".format(chosen_statistic, empire_statistic))
      elif chosen_statistic == 'Crew':
            chosen_statistic = chosen_ship['crew']
            empire_statistic = computer_ship['crew']
            print("Your statistic scores {}, while the Empire's statistic scores {}".format(chosen_statistic, empire_statistic))
      elif chosen_statistic == 'Passengers':
            chosen_statistic = chosen_ship['[passengers']
            empire_statistic = computer_ship['passengers']
            print("Your statistic scores {}, while the Empire's statistic scores {}".format(chosen_statistic, empire_statistic))
      elif chosen_statistic == 'Speed':
            chosen_statistic = chosen_ship['max atmosphering speed']
            empire_statistic = computer_ship['max atmosphering speed']
            print("Your statistic scores {}, while the Empire's statistic scores {}".format(chosen_statistic, empire_statistic))
      elif chosen_statistic == 'Cargo':
            chosen_statistic = chosen_ship['cargo capacity']
            empire_statistic = computer_ship['cargo capacity']
            print("Your statistic scores {}, while the Empire's statistic scores {}".format(chosen_statistic, empire_statistic))


choice_statistic()

#deciding who wins
def battle_cards():
      score = 0
      if chosen_statistic > empire_statistic:
            print("You have won your {} victory against the evil Galactic Empire. "
                  "\nYour score is {}. "
                  "\nBut the battle must continue for peace to be restored to the galaxy...".format(round_count, score + 1))
      elif empire_statistic > chosen_statistic:
            print("You have been defeated by the Empire. "
                  "\nYour score remains {}. "
                  "\nBut do not lose hope, young Jedi. Your time will come to restore peace to the galaxy. ".format(score))

battle_cards()



#tally and present scores so far



