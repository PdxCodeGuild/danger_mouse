import character
import inventory
from room_controller import room_dict
"""
This document contains Item classes for the items in our Danger Mouse game.
The parent class Item defines the subclasses Food and Spell.  
"""


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

    def look(self):
        print('{}: {}'.format(self.name, self.description))

# Fish will be instantiated from the Item class, rather than being a class.
    def action(self, room, character):
        character.inventory.put_in(room.inventory.poplar(self))

class Food(Item):
    """
    Instantiates a Food Item.
    """
    def __init__(self, name):
        scores = {"cheese": 20, "bread": 10, "cake": 30}
        descriptions = {"cheese": "cheese", "bread": "bread", "cake": "cake"}
        super().__init__(name, description = descriptions[name])
        self.score = scores[name]

    def look(self):
        super().look()
        print("Score: {}".format(self.score))

    def rat_nibbling(self):
        """
        Allows a rat to nibble on food in a room.
        """
        score -= 2
        if score <= 0:
            del self
    

    def eat(self, character_who_eats):
        """
        when called on a food item it will decrement the item food value by 5
        takes input character
        """
        if self.score >= 5:
            amount_food = 5
        else:
            amount_food = self.score
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
            {"befriend": "The befriend spell allows you to befriend rats and dogs that \
             will help defend you from cats.", "hide": "The hide spell allows you to hide\
            from everyone in the room.", "scare": "The scare spell will scare people and cats\
            out of the room."}
        super().__init__(name, description = spells[name])

    def cast(self, character_who_casts):
        where_is = room_dict[character_who_casts.location]
        print('You cast {}, so and so is impressed'.format(self.name))
        cast_spell = 'casted_' + character_who_casts.inventory.poplar(self.name).name

        where_is.inventory.put_in_quiet(Item(cast_spell, ""))





class Weapon(Item):
    def __init__(self, name, description, attack = 10):
        super().__init__(name, description, attack)
