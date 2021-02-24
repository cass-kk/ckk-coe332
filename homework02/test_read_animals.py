import unittest
import random
import json
from read_animals3 import breed

class TestBreeding(unittest.TestCase):

    def test_breed(self):

        with open('3animals.json', 'r') as f:
            dict_animals = json.load(f)

        dict1 = random.choice(dict_animals['animals'])
        dict2 = random.choice(dict_animals['animals'])

        self.assertIsInstance(type(breed(dict1, dict2)), dict)
        self.assertIsInstance(type(breed(dict1, dict2).__head__), str)
        self.assertIsInstance(type(breed(dict1, dict2).__body__), str)
        self.assertIsInstance(type(breed(dict1, dict2).__arms__), int)
        self.assertIsInstance(type(breed(dict1, dict2).__legs__), int)

if __name__ == "__main__":
    unittest.main()
