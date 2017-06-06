"""
This document contains Classes for the Characters and Items in our Danger Mouse game.
"""

from random import randrange
from inventory import Inventory

spell_list = ["scare", "hide", "befriend"]

"""The Character class creates characters for our group game."""


class Character:
    def __init__(self, name, description, health=100):
        """
        Initiates a Character object.
        """
        self.description = description
        self.name = name
        self.inventory = Inventory()
        self.health = health

    def move(self):
        """
        Allows a user to choose to leave / enter rooms.
        """
        pass

    def activate(self, room):
        """Runs the ai of a character so it can move and act"""
        pass


class Mouse(Character):
    """
    Instantiates a Mouse or player character.
    """
    def __init__(self, name, description, start_location, health=100):
        """Initiates a Mouse object."""
        super().__init__(name, description, health)
        self.location = start_location
        self.inventory = Inventory()

    def take_food(self, my_food):

        """
        This function works on food items and allows you to eat them and gain
        health or put them in inventory.
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
        # Name is an attribute of object that is a string.
        # Add my_spell to the room inventory,
        # Remove my_spell from the mouse inventory.


class Rat(Character):
    """
    Instanties a Rat character.
    """

    def __init__(self, description, inventory, aggression=randrange(0, 2)):
        super().__init__(self, description, inventory)
        self.agression = aggression

    def activate(self, room):
        """
        Determines how rat interacts with rooms, room inventories (casted spells), and mouse in room.
        """
        # if casted_befriend in room and self.aggression < 3:
        #     self.friend = True
        # elif room contains mouse and casted_hide is not in room:
        #
        # Rats nibble on food and move around randomly, if a cat is in the same
        # room, they will eat the rat and ignore the mouse if its there
        # befriending a rat will have it follow you, beneficial in that it will
        # stop nibbling food and will distract a cat for a turn
        #
        # if rat not friend:
        #   if room contains food and random.randrange(agression, 3) == 2:
        #       nibble on food
        #   else:
        #       move to adjacent room
        # if rat is a friend and mouse isn't in same room:
        #   move rat to mouse
        pass


class Cat(Character):
    def __init__(self, description, aggression=randrange(2, 3)):
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

        # if room contains dog:
        #   print(Dog chases cat away)
        #   dog stops following and starts resting
        #   turns_until_move == 0
        # elif room had a fish in it:
        #   turns_until_move += 3
        #   remove fish
        # elif room contains rat:
        #   rat dies
        # elif room contains mouse and casted_hide is not in room:
        #   attack mouse
        # if casted_scare in room.inventroy and aggression < 3:
        #   cat leaves room
        if turns_until_move == 1 and False:  # And inventory includes bell
            # If the destination room is the room with mouse, alert player
            pass
        if turns_until_move == 0:
            # Move to destination room
            # Generate new destination from list of possible destinations
            turns_until_move = random.randrange(3, 6)
            pass


class Dog(Character):
    searching = 0
    resting = False

    def __init__(self, description, aggression=randrange(1, 4)):
        """
        Instantiates a Dog character.
        """
        super().__init__(self, description, inventory)
        self.agression = aggression

    def activate(self, room):
        """
        Determines how Dog character interacts with room, inventory in room (casted spells), and mouse in room.
        """
        # The dog naps until alerted to a mouse, then alerts nearby human and
        # randomly searches for 5 turns after the mosue escapes
        # If its a friend, it will chase off a cat once before stopping to rest
        #
        # if dog not a friend:
        #   if mouse in same room:
        #       if searching:
        #           atack mouse
        #       bark and alert a nearby human (possibly useful to distract)
        #       searching = 5
        #   elif searching:
        #       searching -= 1
        #       dog moves to adjacent room
        # elif not resting and mouse not in room:
        #   move to mouse
        #
        # if casted_befriend in room and self.aggression < 2:
        #     self.friend = True
        # elif room contains mouse and casted_hide is not in room:
        pass


class Person(Character):
    def __init__(self, description, inventory, aggression=randrange(1, 5)):
        """
        Instantiates a Person character.
        """
        super().__init__(self, description, inventory)
        self.agression = aggression
        seen_mouse = False
        destination = ""
        home_room = ""

    def activate(self, room):
        """
        Determines how Person interacts with rooms, room invenstories (casted spells), and mouse in room.
        """
        # if casted_scare in room and aggression < 3:
        #     leave room
        # elif room contains mouse and casted_hide is not in room:
        #
        # Humans mostly stand still and mind their own business but are still
        # dangerous, either attacking hard or calling other characters nearby.
        # once a mouse leaves a room where the human has seen the mouse, a trap
        # will be laid
        # Humans will also be summoned by barking dogs, if not interrupted by
        # seeing the mouse, they will go to where the dog barked and then back
        #
        # if mouse in room:
        #   either scream to alert others or attack depending on aggression
        #   set destination to current room
        # elif destination is current room:
        #   if seen_mouse:
        #       set trap
        #       seen_mouse = False
        #   else:
        #   destination = home_room
        # if destination is not current room:
        #   move towards destination
        pass
