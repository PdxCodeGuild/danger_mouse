import character
import inventory
"""
This document contains classes for the items in our Danger Mouse game.
"""


class Item:
    def __init__(self, name, description):
        """
        Instantiates new Item.
        """
        self.name = name
        self.description = description

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

    def look(self):
        print('{}: {}'.format(self.name, self.description))

# Fish will be instantiated from the Item class, rather than being a class.
    def action(self, room, character):
        character.inventory.put_in(room.inventory.poplar(self))

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


a_spell = Spell("scare")
print(a_spell)
print(a_spell.description)
