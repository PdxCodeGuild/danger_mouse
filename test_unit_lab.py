import unittest
from character import Dog

class CharacterTest(unittest.TestCase):
    def setup(self):
        self.a_dog = Dog()

    def testCharacter(self):
        self.assertEqual(self.a_dog.name, "dog")
        self.assertEqual(self.a_dog.description, "a dog")
        self.assertEqual(self.a_dog.friend, False)
        self.assertEqual(self.a_dog.resting, False)
        self.assertEqual(self.a_dog.searching, 0)
        self.assertTrue(1 >= self.aggression >= 4)
