import unittest
from character import Dog

class CharacterTest(unittest.TestCase):
    def setUp(self):
        self.a_dog = Dog("kitchen")

    def testCharacter(self):
        self.assertEqual(self.a_dog.name, "dog")
        self.assertEqual(self.a_dog.description, "a dog")
        self.assertEqual(self.a_dog.friend, False)
        self.assertEqual(self.a_dog.resting, False)
        self.assertEqual(self.a_dog.searching, 0)
        self.assertTrue(1 <= self.a_dog.aggression <= 4)
        self.a_dog.activate()
        

if __name__ == '__main__':
    unittest.main()