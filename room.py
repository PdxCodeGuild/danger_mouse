from inventory import Inventory

class Room():
    def __init__(self, description, doors, characters):
        self.description = description
        self.doors = doors
        self.characters = characters
        self.inventory = Inventory()

    def open_door(self, door, inventory): #character.inventory
        if door.is_locked == True and 'door_key' not in inventory:
            print('Door is locked')
        else:
            return door.path


    def peek_room(self, door):
        '''Look around/examine/search room'''
        print(door.path.description)

    def look(self):
        '''Singular/specific inspection for items, doors, etc'''
        print(self.description)



class Door():
    def __init__(self, is_locked, path):
        self.is_locked = is_locked
        self.path = path


        