#Ella's first draft


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

#find way of telling Python which round it is
round_count = 0

allocation_choice = input('Round {round_count}: Would you like to choose your card or be allocated a random one? Type C to choose or R for random. ')

import requests

if allocation_choice == 'C':
      random_card1 = random.randint(1, 36)
      url_1 = 'https://swapi.dev/api/starships/{}/'.format(random_card1)
      response1 = requests.get(url_1)
      starship1 = response1.json()

      random_card2 = random.randint(1, 36)
      url_2 = 'https://swapi.dev/api/starships/{}/'.format(random_card2)
      response2 = requests.get(url_2)
      starship2 = response2.json()

      print(starship1['name'])

      """
      #find way of naming the chosen card ie giving the starship type not the number given to user
      name_r1 = starships['name']

      print('You have a choice between {random_card1} and {random_card2}. ')
      chosen_card = input('Which card do you choose? ')
      url = 'https://swapi.dev/api/starships/{}/'.format(chosen_card)

else allocation_choice == R:
      random_allocated_card = random.randint(1, 36)
      url = 'https://swapi.dev/api/starships/{}/'.format(random_allocated_card)

"""
