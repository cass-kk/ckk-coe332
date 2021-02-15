import json
import petname
import random

dict_animals = {}

arms = []
for i in range(2,11,2):
  arms.append(i)

legs = []
for i in range(3,13,3):
  legs.append(i)

dict_animals['animals'] = []

for i in range(1,21,1):


  heads = ['snake', 'bull', 'lion', 'raven', 'bunny']
  ran_head = random.choice(heads)

  ani = petname.name()
  ani2 = petname.name()
  bodies = ani + ' ' + ani2

  ran_arm = random.choice(arms)

  ran_leg = random.choice(legs)

  tails = ran_arm + ran_leg

  dict_animals['animals'].append({'head': ran_head, 'body':bodies, 'arms': ran_arm, 'legs': ran_leg, 'tails': tails})

with open('animals.json', 'w') as out:
  json.dump(dict_animals, out, indent = 2)
