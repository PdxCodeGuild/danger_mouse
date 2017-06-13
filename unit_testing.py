# Unit Testing:

# Great for testing classes


import unittest
from character import Character, Mouse
from item import Food


class CharacterTest(unittest.TestCase):
    def setUp(self):
        self.player = Character("Chris", "Description", "location")

    def testCharacter(self):
        self.assertEqual(self.player.name, "Chris")
        self.assertEqual(self.player.description, "sdf")


class CharacterTest(unittest.TestCase):
    def setUp(self):
        self.food.item = Food("wedge")
        self.player = Mouse("Chris", "Description", "location")
        self.player.take_item(self.food_item)

    def testCharacter(self):
        self.assertEqual(self.player.name, "Chris")
        self.assertEqual(self.player.description, "sdf")
        self.assertEqual(self.player.health, 100)
        self.player.inventory.bag_of_holding[0].eat(self.player)
        self.assertEqual(self.player.health, 105)

# lab, pick a class that we"ve worked on in the test game and run tests for it
# you might have to fake an input, there is a way to do it
