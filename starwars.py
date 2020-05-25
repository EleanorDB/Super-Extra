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

allocation_choice = input('Round {}: Would you like to choose your card or be allocated a random one? Type C to choose or R for random. '.format(round_count+1))

import requests
"""
# correctly prints starship name for choice
if allocation_choice == 'C' or 'c':
      random_card1 = random.randint(1, 36)
      url_1 = 'https://swapi.dev/api/starships/{}/'.format(random_card1)
      response1 = requests.get(url_1)
      starship1 = response1.json()

      random_card2 = random.randint(1, 36)
      url_2 = 'https://swapi.dev/api/starships/{}/'.format(random_card2)
      response2 = requests.get(url_2)
      starship2 = response2.json()

      #can't get to work: presenting the two choices to user
      #chosen_ship = input("You have a choice between Starship 1: '{}' or Starship 2: '{}'".format(starship1["name"], starship2["name"]))

      #haven't yet tested calling dictionary 
      if chosen_ship == 'Starship 1' or '1':
            stored_choice = {url_1}
      elif chosen_ship == 'Starship 2' or '2':
            stored_choice = {url_2}
      else:
            chosen_ship = input("You have entered an invalid choice. Please type 'Starship 1' or 'Starship 2'.")
            if chosen_ship == 'Starship 1' or '1':
                  stored_choice = {url_1}
            else chosen_ship == 'Starship 2' or '2':
                  stored_choice = {url_2}

#end of choice section 
      """

#if user chooses to be randomly allocated a card
else allocation_choice == 'R' or 'r':
      random_allocated_card = random.randint(1, 36)
      url_rand = 'https://swapi.dev/api/starships/{}/'.format(random_allocated_card)

#giving starship details


