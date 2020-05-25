import random

import requests

#tested opening and works
# print('A long time ago in a galaxy far, far away... '
#       '\nIt is a period of civil war. The Rebellion continue their fight against the evil Galactic Empire.'
#       '\nYou, young Jedi, have been chosen to help the Rebellion in the Battle of Star Wars Top Trumps.'
#       '\nIn some rounds, you must use the Force to choose the starship’s strongest characteristic, which will be compared to the Galactic Empire’s allocated card.'
#       '\nIn other rounds, the Galactic Empire will have the upper hand and will choose the statistic to be compared.'
#       '\nThe side with the highest statistic wins.'
#       '\nYour score will be recorded. Only after choosing 10 winning cards will you succeed in defeating the Empire.'
#       '\nIf you wish to flee the battle scene before the war is won, type: ‘I have lost hope.’'
#       '\nMay the Force be with You.')

#find way of telling Python which round it is
round_count = 0

starship_list = [2, 3, 5, 9, 10, 11, 12, 13, 15, 17]

def random_starship1():
    starship_number1 = random.choice(starship_list)
    url = 'https://swapi.dev/api/starships/{}/'.format(starship_number1)
    response = requests.get(url)
    starship1 = response.json()

    return{
        'name':starship['name'],
        'value':starship['cost_in_credits'],
        'length':starship['length'],
        'max atmosphering speed':starship['max_atmosphering_speed'],
        'max sublight speed (MGLT)':starship['MGLT'],
        'number of crew members':starship['crew'],
        'passengers':starship['passengers'],
        'cargo capacity':starship['cargo_capacity'],
        'hyperdrive rating':starship['hyperdrive_rating'],
    }

def random_starship2():
    starship_number2 = random.choice(starship_list)
    url = 'https://swapi.dev/api/starships/{}/'.format(starship_number2)
    response = requests.get(url)
    starship2 = response.json()

    return{
        'name':starship['name'],
        'value':starship['cost_in_credits'],
        'length':starship['length'],
        'max atmosphering speed':starship['max_atmosphering_speed'],
        'max sublight speed (MGLT)':starship['MGLT'],
        'number of crew members':starship['crew'],
        'passengers':starship['passengers'],
        'cargo capacity':starship['cargo_capacity'],
        'hyperdrive rating':starship['hyperdrive_rating'],
    }

def run():
    my_starship = random_starship()

    print('You were given {}'.format(my_starship['name']))
    stat_choice = input('Which stat do you want to use?')

    opponent_starship = random_starship()
    print('Your opponent has chosen {}'.format(opponent_starship['name']))

    my_stat = my_starship[stat_choice]
    opponent_stat = opponent_starship[stat_choice]

    if my_stat > opponent_stat:
        print('You win!')
    elif my_stat < opponent_stat:
        print('You lose :(')
    else:
        print('Its a draw!')

run()