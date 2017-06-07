from inventory import Inventory

class Room():
    def __init__(self, name,  description, doors, characters):
        self.name = name
        self.description = description
        self.doors = list(doors)
        self.characters = list(characters)
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

    def surroundings(self):
        print(self.description)
        for character in self.characters:
            print(character.name + " is in the room")
        for item in self.inventory.bag_of_holding:
            print(item + " is in the room")
        for door in self.doors:
            print("You can exit through " + door)

    def use_key(self, door, player):
        if door.is_locked == True and player.check_inventory(door.key):
            print('The door is unlocked.')
            door.is_locked = False

    def peek_room(self, door):
        '''Look around/examine/search room'''
        print(door.back.description)
        print(self.characters)

    def look(self):
        '''Singular/specific inspection for items, doors, etc'''
        print(self.name + '\n' +self.description + '\n')
        print('Exits \n')
        for door in self.doors:
            print(door)

    def find_path(self, destination, door_dict):
        # generate dict tree
        nav_tree = {}
        checked = [self]
        level = []
        next_level = []
        nav_tree, checked = self.generate_tree_level(nav_tree, self, door_dict, checked)
        for t in nav_tree[self]:
            level.append(t)

        while level:
            for r in level:
                nav_tree, checked = self.generate_tree_level(nav_tree, r, door_dict, checked)
                for t in nav_tree[r]:
                    next_level.append(t)

            level = next_level
            next_level = []
        print(nav_tree)
        result = self.look_for_destination(nav_tree, self, destination)
        if result:
            return result
        else:
            return "No Path"

    def look_for_destination(self, tree, location, destination):
        if location in tree.keys():
            for r in tree[location]:
                if r == destination:
                    return destination
                else:
                    t = self.look_for_destination(tree, r, destination)
                    if t:
                        path = [r]
                        try:
                            path.extend(t)
                        except TypeError:
                            path.append(t)
                        return path

    def generate_tree_level(self, tree, room, door_dict, checked):
        temp = room.get_adjacent(door_dict, checked)
        for t in temp:
            checked.append(t)
        tree[room] = temp
        return tree, checked

    def get_adjacent(self, door_dict, ignore=[]):
        results = []
        for door in self.doors:
            result = self.open_door(door_dict[door])
            if result != self and result not in ignore:
                results.append(result)
        return results

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
