"""
This document contains Classes for the Characters in our Danger Mouse game.
"""

from random import randrange
from random import choice
from inventory import Inventory


spell_list = ["scare", "hide", "befriend"]

"""The Character class creates characters for our group game."""

# Creates a character. Takes in name, description, location, and health
# {{
class Character:
    def __init__(self, name, description, loc, health=100):
        """
        Initiates a Character object.
        """
        self.location = loc
        self.description = description
        self.name = name
        self.inventory = Inventory(name)
        self.health = health

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
        return "{}".format(self.name)

    def move(self):
        """
        Allows a user to choose to leave / enter rooms.
        """
        pass

    def activate(self, room):
        """Runs the ai of a character so it can move and act"""
        pass

    def look(self):
        print(self.description)

    def die(self):
        pass

    def action(self, room, player):
        print('You try to do something to {} but nothing happens'.format(self))
# }}

# Creates a mouse character
# {{
class Mouse(Character):
    """
    Instantiates a Mouse or player character.
    """
    def __init__(self, name, description, loc, health=100):
        """Initiates a Mouse object."""
        super().__init__(name, description, loc, health)
        self.location = loc
        self.inventory = Inventory(name)

    # {{
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
    # }}

    def take_item(self, my_item):
        """
        This function works on any non-food item, whether spell or fish.
        """
        self.inventory.put_in(my_item)

    def cast_spell(self, my_spell):
        """
        Casts spell by placing a casted spell in the room inventory.
        Charters in room will then be affected by casted_spells in
        room inventory.
        """
        my_spell.name = "casted_" + my_spell.name
        # Name is an attribute of object that is a string.
        # Add my_spell to the room inventory,
        # Remove my_spell from the mouse inventory.

    def attack(self, damage, source):
        health -= damage
# }}

class Rat(Character):
    """
    Instanties a Rat character.
    """

    def __init__(self, name, description, aggression=randrange(0, 2)):
        super().__init__('rat', 'a rat')
        self.aggression = aggression
        self.friend = False

    def activate(self, room):
        """
        Determines how rat interacts with rooms, room inventories
        (casted spells), and mouse in room.
        """

        # Rats nibble on food and move around randomly, if a cat is in the same
        # room, they will eat the rat and ignore the mouse if its there
        # befriending a rat will have it follow you, beneficial in that it will
        # stop nibbling food and will distract a cat for a turn
        #

        room = room_controller.room_dict[self.location]

        if room.check_inventory("casted_befriend") and self.aggression < 3:
            self.friend = True

        if self.friend:
            room_dict = room_controller.room_dict
            for key in room_dict.keys():
                if room_dict[key].get_character_by_type(type(Mouse)):
                    self.location = room_dict[key].get_character_by_type(type(Mouse)).location
        else:
            if room.inventory.find_food() and random.randrange(aggression, 3) == 2:
                room.inventroy.find_food().rat_nibbling()
            else:
                options = room.get_adjacent()
                self.location = options[randrange(0, len(options))].name

        room_controller.room_dict[self.location] = room


class Cat(Character):
    def __init__(self, name, description, loc, aggression=randrange(2, 3)):
        """
        Instantiates a Cat character.
        """
        super().__init__(name, description, loc)
        self.aggression = aggression
        self.turns_until_move = randrange(3, 6)
        self.destination = ""

    def activate(self, room):
        """
        Determines how cat interacts with rooms, inventories in rooms (casted
        spells), and mouse in room.
        """

        room = room_controller.room_dict[self.location]

        if not self.destination:
            destinations = room_controller.room_dict.keys()
            destinations.pop(self.location)
            while not self.destination:
                temp = choice(destinations)
                if room.find_path(self.destination, room_controller.door_dict):
                    self.destination = temp

        if room.check_inventory("casted_scare") and aggression < 3:
            turns_until_move = 0
        elif room.get_character_by_type(type(Dog)):
            print("Dog chases cat away")
            turns_until_move = 0
            if room.get_character_by_type(type(Dog)).friend:
                room.get_character_by_type(type(Dog)).resting = True
        elif room.check_inventory("fish"):
            turns_until_move += 3
            room.inventory.poplar("fish")
        elif room.get_character_by_type(type(Rat)):
            room.get_character_by_type(type(Rat)).die()
        elif mouse in room.characters and not room.inventory.check_inventory(casted_hide):
            pass
            # attack mouse
        else:
            turns_until_move -= 1

        # if turns_until_move == 1 and self.inventory.check_inventory("bell"):  # And inventory includes bell
        #     # If the destination room is the room with mouse, alert player
        #     pass
        if turns_until_move == 0:
            self.location = self.destination
            self.destination = ""
            self.turns_until_move = randrange(3, 6)
            pass

        room_controller.room_dict[self.location] = room


class Dog(Character):
    searching = 0
    resting = False

    def __init__(self, name, description, loc, aggression=randrange(1, 4)):
        """
        Instantiates a Dog character.
        """
        super().__init__("dog", "a dog", inventory, loc)
        self.aggression = aggression
        self.friend = False
        self.resting = False
        self.searching = 0

    def activate(self, room):
        """
        Determines how Dog character interacts with room, inventory in room
        (casted spells), and mouse in room.
        """
        room = room_controller.room_dict[self.location]
        room_dict = room_controller.room_dict

        # The dog naps until alerted to a mouse, then alerts nearby human and
        # randomly searches for 5 turns after the mosue escapes
        # If its a friend, it will chase off a cat once before stopping to rest

        if not self.friend:
            if room.get_character_by_type(type(Mouse)) and not room.check_inventory("casted_hide"):
                if self.searching:
                    # attack mouse
                    for key in room_dict.keys():
                        if room_dict[key].get_character_by_type(type(Human)):
                            print("BARK")
                            room_controller.room_dict[key].get_character_by_type(type(Human)).path = room_dict[key].find_path(room)
                    searching = 1 + self.aggression
            elif self.searching:
                self.searching -= 1
                self.location = choice(room.get_adjacent).name
        elif not self.resting:
            for key in room_dict.keys():
                if room_dict[key].get_character_by_type(type(Mouse)):
                    self.location = room_dict[key].get_character_by_type(type(Mouse)).location

        if room.inventory.check_inventory("casted_befriend") and self.aggression < 2:
            self.friend = True
            self.resting = False
        room_controller.room_dict[self.location] = room


class Person(Character):
    def __init__(self, name, description, inventory, loc, aggression=randrange(1, 5)):
        """
        Instantiates a Person character.
        """
        super().__init__("person", "a person", inventory, loc)
        self.aggression = aggression
        self.seen_mouse = False
        self.path = ""
        self.home_room = ""

    def activate(self, room):
        """
        Determines how Person interacts with rooms, room invenstories
        (casted spells), and mouse in room.
        """
        # Humans mostly stand still and mind their own business but are still
        # dangerous, either attacking hard or calling other characters nearby.
        # once a mouse leaves a room where the human has seen the mouse, a trap
        # will be laid
        # Humans will also be summoned by barking dogs, if not interrupted by
        # seeing the mouse, they will go to where the dog barked and then back
        #
        room = room_controller.room_dict[self.location]
        room_dict = room_controller.room_dict
        if room.inventory.check_inventory(casted_scare) and self.aggression < 3:
            # set a random destination
            pass
        elif room.get_character_by_type(type(mouse)) and not room.check_inventory("casted_hide"):
            if self.aggression <= 2:
                for key in room_dict.keys():
                    if room_dict[key].get_character_by_type(type(Cat)):
                        print("SCREAM")
                        room_controller.room_dict[key].get_character_by_type(type(Cat)).destination = location
                        room_controller.room_dict[key].get_character_by_type(type(Cat)).turns_until_move = 0
                    else:
                        # attack mouse
                        path = location
                        seen_mouse = True
        elif self.path:
            self.location = self.path.pop(0)
        else:
            if seen_mouse:
                # set trap
                seen_mouse = False
            else:
                self.path = room_dict[self.location].find_path(room_dict[home_room], room_controller.door_dict)
        room_controller.room_dict[self.location] = room
