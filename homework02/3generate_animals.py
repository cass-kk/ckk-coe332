#!/usr/bin/env python3
import json
import petname
import random
import sys

def main():

    dict_animals = {}
    dict_animals['animals'] = []

    arms = []
    for i in range(2,11,2):
        arms.append(i)
    
    legs = []
    for i in range(3,13,3):
        legs.append(i)

    for i in range(1,21,1):
        
        indiv_animal = {}

        indiv_animal['head'] = random.choice(['snake', 'bull', 'lion', 'raven', 'bunny'])

        indiv_animal['body'] = petname.name() + '-' + petname.name()
        
        indiv_animal['arms']  = random.choice(arms)
        
        indiv_animal['legs'] = random.choice(legs)

        indiv_animal['tails'] = indiv_animal['arms'] + indiv_animal['legs']
        
        dict_animals['animals'].append(indiv_animal)
        
        
    with open(sys.argv[1], 'w') as f:
        json.dump(dict_animals, f, indent=2)

if __name__ == "__main__":
    main()
