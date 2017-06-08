import character
import inventory
from room_controller import room_dict
"""
This document contains Item classes for the items in our Danger Mouse game.
The parent class Item defines the subclasses Food and Spell.  
"""

# This creates an item with a name and description. The default
# 'attack' damage for non-weapons is 2. The only item that is in the
# 'item' class is fish, everything else is in a child class
# {{
class Item:
    def __init__(self, name, description, attack = 2):
        """
        Instantiates new Item.
        """
        self.name = name
        self.description = description
        self.attack = attack

    def __str__(self):
        """
        Overloads print function.
        """
        return self.name

    def __repr__(self):
        """
        Determines what the representation will be when it's in a list.
        """
        return self.__str__()

    # Prints the item's name and description
    # {{
    def look(self):
        print('{}: {}'.format(self.name, self.description))
    # }}

    # 'action' takes an item from the room's inventory
    # {{
    def action(self, room, character):
        character.inventory.put_in(room.inventory.poplar(self))
    # }}
# }}


# Creates a food item
# {{
class Food(Item):
    """
    Instantiates a Food Item.
    """
    # When creating a food item, it takes in the 'name' variable,
    # and uses dictionaries to get information to create the super class
    # {{
    def __init__(self, name):
        scores = {"cheese": 20, "bread": 10, "cake": 30}
        descriptions = {"cheese": "cheese", "bread": "bread", "cake": "cake"}
        super().__init__(name, description = descriptions[name])
        self.score = scores[name]
    # }}


    # This version of look prints the foods score in addition to the name
    # the description
    # {{
    def look(self):
        super().look()
        print("Score: {}".format(self.score))
    # }}



    # This is used to allow rats to nibble at food. The food wastes away
    # Until it's score is less than zero
    # {{
    def rat_nibbling(self):
        """
        Allows a rat to nibble on food in a room.
        """
        score -= 2
        if score <= 0:
            del self
    # }}
    
# }}

# input a character, that character eats food
# {{
    def eat(self, character_who_eats):
        """
        when called on a food item it will decrement the item food value by 5
        takes input character
        """

        # When you eat food, it loses 5 score, and you gain 5 health.
        # If the food's score is 1, you get 1 more heath
        # If the food's score goes to zero, the food is deleted
        # {{
        amount_food = 5
        if self.score >= 5:
            amount_food = 5
        else:
            amount_food = self.score
        self.score -= amount_food
        character_who_eats.health += amount_food
        if self.score <= 0:
            character_who_eats.inventory.poplar(self.name)
        # }}

# }}

# TODO:  The inventory still needs a way to calculate
#        the total store to win the game.

# Creates a spell item. It creates the description based on the name
# {{
class Spell(Item):
    def __init__(self, name):
        """
        Instantiates a spell item.
        """
        spells = \
            {"befriend": "The befriend spell allows you to befriend rats and dogs that \
             will help defend you from cats.", "hide": "The hide spell allows you to hide\
            from everyone in the room.", "scare": "The scare spell will scare people and cats\
            out of the room."}
        super().__init__(name, description = spells[name])

    # Input the character who casts, print a message, and the
    # spell moves from the player's inventory to the room's inventory
    # {{
    def cast(self, character_who_casts):
        where_is = room_dict[character_who_casts.location]
        print('You cast {}, so and so is impressed'.format(self.name))
        cast_spell = 'casted_' + character_who_casts.inventory.poplar(self.name).name

        where_is.inventory.put_in_quiet(Item(cast_spell, ""))
    # }}


# }}



# Creates a weapon with an attack value of ten
# {{
class Weapon(Item):
    def __init__(self, name, description, attack = 10):
        super().__init__(name, description, attack)
# }}
