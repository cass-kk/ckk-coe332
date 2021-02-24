#!/usr/bin/env python3
import json
import random
import sys


def breed(dict1, dict2):
    offspring = {}
    offspring['head'] = random.choice([dict1['head'], dict2['head']])
    offspring['body'] = random.choice([dict1['body'], dict2['body']])
    offspring['arms'] = random.choice([dict1['arms'], dict2['arms']])
    offspring['legs'] = random.choice([dict1['legs'], dict2['legs']])
    offspring['tails'] = offspring['legs'] + offspring['arms']
    return(offspring)

def main():

    with open(sys.argv[1], 'r') as f:
        dict_animals = json.load(f)

    print("Random animal: ", random.choice(dict_animals['animals']))

    dict1 = random.choice(dict_animals['animals'])
    print("Parent 1: ", dict1)
    dict2 = random.choice(dict_animals['animals'])
    print("Parent 2: ", dict2)

    dict_animals['offspring'] = []
    offspring = breed(dict1, dict2)
    dict_animals['offspring'].append(offspring)
    print("Offspring of Parents 1 and 2: ", dict_animals['offspring'])

if __name__ == "__main__":
    main()
