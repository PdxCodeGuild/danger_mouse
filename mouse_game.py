"""The character class creates characters for our group game."""

from random import randrange

aggression = random.randrange(1, 5)


class Character:
    def __init__(self, name, description, inventory, health=100):
        self.description = description
        self.name = name
        self.inventory = list(inventory)
        self.health = health

    def move(self):
        """Allows a user to choose to leave / enter rooms."""
        pass

    def activate(self, room):
        """Runs the ai of a character so it can move and act"""
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


class Rat(Character):
    def __init__(self, description, inventory, aggression=randrange(0, 2)):
        super().__init__(self, description, inventory)
        aggression = self.agression

    def activate(self, room):
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
    def __init__(self, description, aggression=random.randrange(2, 3)):
        super().__init__(self, description, inventory)
        aggression = self.agression
        turns_until_move = random.randrange(3, 6)
        destination = ""

    def activate(self, room):
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
        # elif room contains unhidden mouse:
        #   attack mouse
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

    def __init__(self, description, aggression=random.randrange(1, 4)):
        super().__init__(self, description, inventory)
        aggression = self.agression

    def activate(self, room):
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
        pass


class Person(Character):
    def __init__(self, description, inventory, aggression=randrange(1, 5)):
        super().__init__(self, description, inventory)
        aggression = self.agression
        seen_mouse = False
        destination = ""
        home_room = ""

    def activate(self, room):
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


class Item:
    def __init__(self, name):
        name = self.name
        value = self.value


class Food(Item):
    def __init__(self, name, score):
        self.name = name
        # self.description = description
        self.score = score

    def take_food(self):
        choice = input("Add to health(h) or inventory(i)?")
        if choice == "h":
            self.health += self.score
        elif choice == "i":
            self.inventory.append(name)
        print(self.health, self.inventory)

    def __str__(self):
        return "{}".format(self.name)
        # this puts those values into a string, which you need

    def __repr__(self):
        # this is what the representation will be when it's in a list
        return self.__str__()


class Spell(Item):

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def take_spell(self):
        pass

    # elif name == "fish":
    # elif name == "scare":
    # elif name == "hide":
    # elif name == "befriend":


horace = Mouse("Rasputin", "A wise mouse.", ["befriend"])
# horace.find_item("bread")
bread = Food("bread", 20)
horace.take_food(bread)
print(horace.inventory[1].name)
