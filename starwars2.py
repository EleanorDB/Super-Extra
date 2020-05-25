#Ella's second draft Mon 25 May

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


round_count = 0

allocation_choice = input('Round {}: Would you like to choose your card or be allocated a random one? Type C to choose or R for random. '.format(round_count+1))

import requests

starship_list=[2, 3, 5, 9, 10, 11, 12, 13, 15, 17]

def random_starship1():
    starship_number1 = random.choice(starship_list)
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

def random_starship2():
    starship_number2 = random.choice(starship_list)
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


def card_choice():
    if allocation_choice == 'C' or 'c':
        chosen_card = input("You have a choice between Starship 1: '{}' or Starship 2: '{}'".format(starship1['name'], starship2['name']))
        print(chosen_card)
    elif allocation_choice == 'R' or 'r':
        print("You have been allocated the following Starship: '{}'".format(starship1['name']))
    else:
        print("You have entered an invalid response. Please type 'C' to choose or 'R' to be randomly allocated a starship.")


card_choice()

