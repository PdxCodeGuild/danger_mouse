from inventory import Inventory

class Room():
    def __init__(self, name,  description, doors, characters):
        self.name = name
        self.description = description
        self.doors = doors
        self.characters = characters
        self.inventory = Inventory(name)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def open_door(self, door): #character.inventory
        if door.is_locked == True:
            print('Door is locked.')
        else:
            if self.name == door.front.name:
                return door.back
            if self.name == door.back.name:
                return door.front
        return self

    def add_item(self, item):
        self.inventory.put_in(item)

    def update_characters(self, characters):
        self.characters = list(characters)

    def remove_item(self, item):
        self.inventory.poplar(item)

    def check_inventory(self, item):
        self.inventory.check_inventory(item)

    def look(self):
        print(self.description)
        for character in self.characters:
            print("{} is in the room".format(character))
        for item in self.inventory.bag_of_holding:
            print("{} is in the room".format(item))
        for door in self.doors:
            print("You can exit through {}".format(door))

    def use_key(self, door, player):
        if door.is_locked == True and player.check_inventory(door.key):
            print('The door is unlocked.')
            door.is_locked = False
        if door.is_locked == False:
            print('The door is already unlocked')

    def peek_room(self, door):
        '''Look around/examine/search room'''
        print(door.back.name)
        for character in self.characters:
            print('characters in room: {}'.format(character))

    # def look(self):
    #     '''Singular/specific inspection for items, doors, etc'''
    #     print(self.name + '\n' +self.description + '\n')
    #     print('Exits')
    #     for door in self.doors:
    #         print(door)


#We can add time to add a dificulty to some doors, say like the one to the treasure chest.
#and opening size, maybe the cat can't fit through some. We could also change the front and back room
#and create doors that go more than three places. A teleporter maybe?

class Door():
    def __init__(self,name, description, room1, room2, is_locked, key):
        self.name = name
        self.description = description
        self.front = room1
        self.back = room2
        self.is_locked = is_locked
        self.key = key

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def look(self):
        print(self.name + '/n' + self.description)

    def action(self, room, player):
        room.use_key(self, player)

