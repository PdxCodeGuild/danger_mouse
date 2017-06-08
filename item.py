import character
import inventory
"""
This document contains classes for the items in our Danger Mouse game.
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

    def eat(self, character_who_eats):
        """
        when called on a food item it will decrement the item food value by 5
        takes input character
        """

        amount_food = 5
        self.score -= amount_food
        character_who_eats.health += amount_food
        if self.score <= 0:
            character_who_eats.inventory.poplar(self.name)



# TODO:  The inventory still needs a way to calculate
#        the total store to win the game.


class Spell(Item):
    def __init__(self, name):
        """
        Instantiates a spell item.
        """
        spells = \
            {"befriend": "The befriend spell allows you to befriend rats and dogs that "
            "will help defend you from cats.", "hide": "The hide spell allows you to hide "
            "from everyone in the room.", "scare": "The scare spell will scare people and cats "
            "out of the room."}
        super().__init__(name, description = spells[name])


class Weapon(Item):
    def __init__(self, name, description, attack = 10):
        super().__init__(name, description, attack)
