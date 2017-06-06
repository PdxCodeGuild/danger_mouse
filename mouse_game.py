"""
This document contains Classes for the Characters and Items in our Danger Mouse game.
"""

import random

aggression=random.randrange(1, 5)

spell_list = ["scare", "hide", "befriend"]


"""The Character class creates characters for our group game."""

class Character:
    def __init__(self, name, description, inventory, health=100):
        """
        Initiates a Character object.
        """
        self.description = description
        self.name = name
        self.inventory = list(inventory)
        self.health = health

    def move(self):
        """
        Allows a user to choose to leave / enter rooms.
        """
        pass

    def auto_move(self):
        """
        Computer automatically chooses a move.
        """
        pass


class Mouse(Character):
    """
    Instantiates a Mouse or player character.
    """
    def __init__(self, name, description, inventory, health=100):
        """Initiates a Mouse object."""
        super().__init__(name, description, inventory, health)


    def take_food(self, my_food):

        """
        This function works on food items and allows you to eat them and gain health or put them in inventory.
        """

        choice = input("Add to health(h) or inventory(i)?")
        if choice == "h":
            self.health += my_food.score
            return self.health
        elif choice == "i":
            self.inventory.append(my_food)
            return self.inventory

    def take_item(self, my_item):
        """
        This function works on any non-food item, whether spell or fish.
        """
        self.inventory.append(str(my_item))
        return self.inventory


    def cast_spell(self, my_spell):
        """
        Casts spell by placing a casted spell in the room inventory.
        Charters in room will then be affected by casted_spells in room inventory.
        """
        my_spell.name = "casted_" + my_spell.name
        #Name is an attribute of object that is a string.
        #Add my_spell to the room inventory,
        #Remove my_spell from the mouse inventory.


class Rat(Character):
    """
    Instanties a Rat character.
    """
    def __init__(self, description, inventory, aggression=random.randrange(1, 2)):
        super().__init__(self, description, inventory)
        aggression = self.agression


    def activate(self, room):
        """
        Determines how rat interacts with rooms, room inventories (casted spells), and mouse in room.
        """
        # if casted_befriend in room and self.aggression < 3:
        #     self.friend = True
        # elif room contains mouse and casted_hide is not in room:
        pass



class Cat(Character):
    def __init__(self, description, aggression=random.randrange(2, 3)):
        """
        Instantiates a Cat character.
        """
        super().__init__(self, description, inventory)
        self.agression = aggression
        turns_until_move = random.randrange(3, 6)
        destination = ""

    def activate(self, room):
        """
        Determines how cat interacts with rooms, inventories in rooms (casted spells), and mouse in room.
        """
        if not destination:
            # generate destination
            pass
        # if room had a fish in it:
        # turns_until_move += 3
        # if room contains dog:
        # print(Dog chases cat away)
        # turns_until_move == 0
        # elif room contains rat:
        # cat eats rat
        # elif room contains mouse and casted_hide is not in room:
        # attack mouse
        # if casted_scare in room and aggression < 3:
        #     leave room
        if turns_until_move == 1 and False:  # And inventory includes bell
            # If the destination room is the active room, alert player
            pass
        if turns_until_move == 0:
            # Move to destination room
            # Generate new destination
            turns_until_move = random.randrange(3, 6)
            pass


class Dog(Character):
    def __init__(self, description, aggression=random.randrange(1, 4)):
        """
        Instantiates a Dog character.
        """
        super().__init__(self, description, inventory)
        aggression = self.agression

    def activate(self, room):
        """
        Determines how Dog character interacts with room, inventory in room (casted spells), and mouse in room.
        """
        # if casted_befriend in room and self.aggression < 2:
        #     self.friend = True
        # elif room contains mouse and casted_hide is not in room:
        pass



class Person(Character):
    def __init__(self, description, inventory, aggression=random.randrange(1, 5)):
        """
        Instantiates a Person character.
        """
        super().__init__(self, description, inventory)
        self.agression = aggression

    def activate(self, room):
        """
        Determines how Person interacts with rooms, room invenstories (casted spells), and mouse in room.
        """
        # if casted_scare in room and aggression < 3:
        #     leave room
        # elif room contains mouse and casted_hide is not in room:
        pass


class Item:
    def __init__(self, name):
        """
        Instantiates new Item.
        """
        self.name = name

    def __str__(self):
        """
        Overloads print function.
        """
        return "{}".format(self.name)
        # this puts those values into a string, which you need

    def __repr__(self):
        """
        Determines what the representation will be when it's in a list.
        """
        return self.__str__()

#Fish will be instantiated from the Item class, rather than being a class.

class Food(Item):
    """
    Instantiates a Food Item.
    """
    def __init__(self, score,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.score = score

    def rat_nibbling(self):
        """
        Allows a rat to nibble on food in a room.
        """
        score -= 2
        if score <= 0:
            del self

# TODO:  The inventory still needs a way to calculate the total store to win the game.


class Spell(Item):
    def __init__(self, name):
        """
        Instantiates a spell item.
        """
        super().__init__(name)
