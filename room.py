from inventory import Inventory

class Room():
    def __init__(self, name,  description, doors, characters = None):
        self.name = name
        self.description = description
        self.doors = room_map[name]
        self.characters = list(characters)
        self.inventory = Inventory()


    def open_door(self, door): #character.inventory
        if door.is_locked == True and not self.inventory.check_inventory(door.key):
            print('Door is locked.')
        else:
            print('The door is unlocked.')
            return door.path



    def peek_room(self, door):
        '''Look around/examine/search room'''
        print(door.room2.description)

    def look(self):
        '''Singular/specific inspection for items, doors, etc'''
        print(self.name + '\n' +self.description + '\n')
        print('Exits \n')
        for door in self.doors:
            print(door.name + '\n')


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
        self.key

    def look(self):
        print(self.name + '/n' + self.description)


#This dictionary is the begining of a graph. The rooms would be the nodes and the doors the edges.
#
room_map = {    'nest': ['library'],
                'library': ['east_hall', 'nest'],
                'east_hall': ['library', 'serv_camber', 'gallery', 'guest_bedroom', 'master_bedroom', 'main_hall'],
                'serv_chamber': ['east_hall', 'servant_hall'],
                'gallery': ['east_hall'],
                'guest_bedroom': ['east_hall'],
                'master_bedroom': ['east_hall', 'chest_one', 'dresser'],
                'main_hall': ['east_hall', 'living_room', 'outside'],
                'living_room': ['main_hall', 'chapel'],
                'chapel': ['living_room', 'west_hall'],
                'west_hall': ['chapel', 'kitchen'],
                'kitchen': ['west_hall', 'buttery', 'servant_hall'],
                'servant_hall': ['serv_chamber', 'kitchen'],
                'dresser': ['master_bedroom']
                }
