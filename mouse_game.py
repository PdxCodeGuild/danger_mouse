"""The character class creates characters for our group game."""

import random

aggression=random.randrange(1, 5)

spell_list = ["scare", "hide", "befriend"]

class Character:
    def __init__(self, name, description, inventory, health=100):
        self.description = description
        self.name = name
        self.inventory = list(inventory)
        self.health = health

    def move(self):
        """Allows a user to choose to leave / enter rooms."""
        pass

    def auto_move(self):
        """Computer automatically chooses a move."""
        pass


class Mouse(Character):
    def __init__(self, name, description, inventory, health=100):
        super().__init__(name, description, inventory, health)


    def take_food(self, my_food):
        choice = input("Add to health(h) or inventory(i)?")
        if choice == "h":
            self.health += my_food.score
            return self.health
        elif choice == "i":
            self.inventory.append(my_food)
            return self.inventory


    def take_spell(self, my_spell):
        # if my_spell in spell_list:
        self.inventory.append(my_spell)
        return self.inventory

        # elif my_spell == "fish":
        #     #This will add fish to room inventory
        #     pass


class Rat(Character):
    def __init__(self, description, inventory, aggression=random.randrange(1, 2)):
        super().__init__(self, description, inventory)
        aggression = self.agression

    def activate(self, room):
        pass


class Cat(Character):
    def __init__(self, description, aggression=random.randrange(2, 3)):
        super().__init__(self, description, inventory)
        aggression = self.agression
        turns_until_move = random.randrange(3, 6)
        destination = ""

    def activate(self, room):
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
        # elif room contains mouse:
        # attack mouse
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
        super().__init__(self, description, inventory)
        aggression = self.agression

    def activate(self, room):
        pass


class Person(Character):
    def __init__(self, description, inventory, aggression=random.randrange(1, 5)):
        super().__init__(self, description, inventory)
        self.agression = aggression

    def activate(self, room):
        pass


class Item:
    def __init__(self, name):
        self.name = name


class Food(Item):


    def __init__(self, score,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.score = score


    def __str__(self):
        return "{}".format(self.name)
        # this puts those values into a string, which you need


    def __repr__(self):
        # this is what the representation will be when it's in a list
        return self.__str__()


#The inventory still needs a way to calculate the total store to win the game.


class Spell(Item):
    def __init__(self, name):
        super().__init__(name)



