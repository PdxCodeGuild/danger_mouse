import room
import csv

#This dictionary is the begining of a graph. The rooms would be the nodes and the doors the edges.
#
# print(room.generate_doors(room.room_map))


with open('rooms_sheet.csv') as csvfile:
    room_importer = csv.reader(csvfile, delimiter = ',')
    room_dict = {}
    for row in room_importer:
        temp = room.Room(row[0], row[1], room.room_map[row[0], row[2])
        room_dict[row[0]] = temp

game_over = False
current_room = room_dict['nest']
while not game_over:
    current_room.look()
    user_input = ' '.split(input('What is  your command?'))
    first = user_input[0]
    second = user_input[1]

    if first == 'Open':
        current_room = current_room.open_door(second)
    if first == 'look':
        if second == 'room':
            current_room.look()
        if second in current_room.doors:
            print("it is a door")
        if second in current_room.characters:
            print('this is a character')
    if first == 'peek':
        current_room.peek(room_dict[second])



