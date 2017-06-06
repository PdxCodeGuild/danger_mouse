import room
import csv

#This dictionary is the begining of a graph. The rooms would be the nodes and the doors the edges.
#
# print(room.generate_doors(room.room_map))


# with open('rooms_sheet.csv') as csvfile:
#     room_importer = csv.reader(csvfile, delimiter = ',')
#     room_dict = {}
#     for row in room_importer:
#         temp = room.Room(row[0], row[1], room.room_map[row[0]], row[2])
#         room_dict[row[0]] = temp
nest = room.Room('nest', 'Home sweet home', room.room_map['nest'], [])
library = room.Room('library', 'Lots of books', room.room_map['library'], [])
east_hall = room.Room('east_hall', 'Dark Hallway', room.room_map['east_hall'], [])
serv_chamber = room.Room('serv_chamber', 'The room for the help', room.room_map['serv_chamber'], [])
gallery = room.Room('gallery', 'Pretty Art', room.room_map['gallery'], [])
guest_bedroom = room.Room('guest_bedroom', 'A small room', room.room_map['guest_bedroom'], [])
master_bedroom = room.Room('master_bedroom', 'A bedroom with a large bed', room.room_map['master_bedroom'], [])
grand_hall = room.Room('grand_hall', 'A large Atrium', room.room_map['grand_hall'], [])
living_room = room.Room('living_room', 'Couches and stuff', room.room_map['living_room'], [])
chapel = room.Room('chapel', 'Flying Spaghetti Monster', room.room_map['chapel'], [])
west_hall = room.Room('west_hall', 'creeky hallway', room.room_map['west_hall'], [])
kitchen = room.Room('kitchen', 'There must be cheese somewhere', room.room_map['kitchen'], [])
servant_hall = room.Room('servant_hall', 'A shortcut', room.room_map['servant_hall'], [])
dresser = room.Room('dresser', 'Filled with clothes', room.room_map['dresser'], [])
buttery = room.Room('buttery', 'Filled with cheese', room.room_map['butter'], [])
home_door = room.Door('home_door', 'Sign says Welcome', nest, library, False)
library_door = room.Door('library_door', 'A crack under the door', library, east_hall, False)
swinging_door = room.Door('swinging_door', 'A swinging door', east_hall, grand_hall, False)
servant_door = room.Door('servant_door', 'A wooden door', east_hall, serv_chamber, True)
gallery_door = room.Door('gallery_door', 'It looks like you can squeze through the door', east_hall, gallery, False)
guest_door = room.Door('guest_door', 'A wooden door', east_hall, guest_bedroom, False)
master_door = room.Door('master_door', 'A wooden door', east_hall, master_bedroom, True)
grand_arch = room.Door('grand_arch', 'A large archway', grand_hall, living_room, False)
chapel_door = room.Door('chapel_door', 'A thick door', living_room, chapel, False)
fsm_door = room.Door('fsm_door', 'The flying speghetti monster rests on the door', chapel, west_hall, False)
kitchen_entry = room.Door('kitchen_entry', 'A swinging double door', west_hall, kitchen, False)
buttery_entry = room.Door('butter_entry', 'One more door', kitchen, buttery,)

room_dict ={'nest': nest,
            'library': library,
            'east_hall': east_hall,
            'serv_chamber': serv_chamber,
            'gallery': gallery,
            'guest_bedroom': guest_bedroom,
            'master_bedroom': master_bedroom,
            'grand_hall': grand_hall,
            'living_room': living_room,
            'chapel': chapel,
            'west_hall': west_hall,
            'kitchen': kitchen,
            'servant_hall': servant_hall,
            'dresser': dresser
            }


game_over = False
current_room = room_dict['nest']
while not game_over:
    current_room.look()
    user_input = (input('What is  your command?')).split(' ')
    print(user_input)
    first = user_input[0]
    second = user_input[1]

    if first == 'open':
        current_room = current_room.open_door(room_dict[second])
    if first == 'look':
        if second == 'room':
            current_room.look()
        if second in current_room.doors:
            print("it is a door")
        if second in current_room.characters:
            print('this is a character')
    if first == 'peek':
        current_room.peek(room_dict[second])




