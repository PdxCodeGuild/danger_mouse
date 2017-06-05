"""The character class creates characters for our group game."""

import random

aggression=random.randrange(1, 5)

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
        aggression = self.agression

    def activate(self, room):
        pass


class Item:
    def __init__(self, name):
        name = self.name
        value = self.value


class Food(Item):
    def __init__(self, name, score):
        self.name = name
        self.description = description
        self.score = score

    def take_food(self):
        choice = input("Add to health(h) or inventory(i)?")
        if choice == "h":
            self.health += self.score
        elif choice == "i":
            self.inventory.append(name)
        print(self.health, self.inventory)

class Spell(Item):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def take_spell(self):



foods = {"bread": 20, ""}
        if name == "bread":
            choice = input("Add to health(h) or inventory(i)?")
            if choice == "h":
                self.health += 20
            elif choice == "i":
                self.inventory.append(name)
            print(self.health, self.inventory)

    # elif name == "cheese":
    #     character.health += 30
    #     character.inventory[0] += 30
    # elif name == "cake":
    #     character.health += 50
    #     character.inventory[0] += 20
    #
    # elif name == "fish":
    #
    #
    # elif name == "scare":
    # elif name == "hide":
    # elif name == "befriend":

horace = Mouse("Rasputin", "A wise mouse.", ["befriend"])
horace.find_item("bread")
