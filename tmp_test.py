class Room:
    def __init__(self, name, doors, desc):
        self.name = name
        self.doors = doors
        self.desc = desc


class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location

start_room = Room('Start Room', {}, 'A big empty room')

second_room = Room('Second Room', {}, 'There is like snakes and stuff. Eww.')

start_room.doors = {'north': second_room}
second_room.doors = {'south': start_room}


player = Player('Chris', start_room)


while True:
    print('You are in {}. {}'.format(player.location.name, player.location.desc))
    q = input('You can (L)ook around or (M)ove: ')

    if q.lower() == 'm':
        print('You see exits:')
        for k, v in player.location.doors.items():
            print('{}'.format(k))
            ch = input('Where would you like to move?: ')
            player.location = player.location.doors[ch]

