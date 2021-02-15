import json
import random

with open('animals.json', 'r') as f:
    dict_animals = json.load(f)

options = []
for i in range(1,21,1):
    options.append(i)

n = random.choice(options)

print(dict_animals['animals'][n])
