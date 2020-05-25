import random

import requests

starship_list=[2, 3, 5, 9, 10, 11, 12, 13, 15, 17]

def random_starship():
    starship_number = random.choice(starship_list)
    url = 'https://swapi.dev/api/starships/{}/'.format(starship_number)
    response = requests.get(url)
    starship = response.json()

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