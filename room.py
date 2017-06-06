from inventory import Inventory

class Room():
    def __init__(self, name,  description, doors, characters):
        self.name = name
        self.description = description
        self.doors = doors
        self.characters = characters
        self.inventory = Inventory()


    def open_door(self, door): #character.inventory
        if door.is_locked == True:
            print('Door is locked.')
        else:
            if self.name == door.front.name:
                return door.back
            if self.name == door.back.name:
                return door.front

    def use_key(self, door):
        if door.is_locked == True and self.inventory.check_inventory(door.key):
            print('The door is unlocked.')
            door.is_locked = False
            
    def peek_room(self, door):
        '''Look around/examine/search room'''
        print(door.back.description)

    def look(self):
        '''Singular/specific inspection for items, doors, etc'''
        print(self.name + '\n' +self.description + '\n')
        print('Exits \n')
        for door in self.doors:
            print(door + '\n')


#We can add time to add a dificulty to some doors, say like the one to the treasure chest.
#and opening size, maybe the cat can't fit through some. We could also change the front and back room
#and create doors that go more than three places. A teleporter maybe?

class Door():
    def __init__(self,name, description, room1, room2, is_locked):
        self.name = name
        self.description = description
        self.front = room1
        self.back = room2
        self.is_locked = is_locked
        # self.key

    def look(self):
        print(self.name + '/n' + self.description)
