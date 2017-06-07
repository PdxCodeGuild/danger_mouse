"""
This document contains Classes for the items in our Danger Mouse game.
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
        return "{}".format(self.name)
        # this puts those values into a string, which you need

    def __repr__(self):
        """
        Determines what the representation will be when it's in a list.
        """
        return self.__str__()

    def look(self):
        return self.description
# Fish will be instantiated from the Item class, rather than being a class.


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
        super().__init__(name)


class Scare(Spell):
    """
    This class represents the Scare Spell.
    """
    def cast_spell(self, target):
        if target.aggression <= 2:  # if the target's aggression level is low, it escapes
            target.move(destination)
        else:
            self.inventory.owner.health -= target.agression * 3  # if character's aggression level is high, mouse loses health points.


class Hide(Spell):
    """
    This class represents Hide Spell.
    """
    def cast_spell(self, character):
        character.move(destination)



class Befriend(Spell):
    """
    This class represents Befriend Spell.
    """
    def cast_spell(self, target):
        if target.agression <= 2:
            self.inventory.owner.health += target.agression * 3  # if character's aggression level is low, mouse gains health points.
        else:
            print("{} is not in the mood to make friends".format(target))


