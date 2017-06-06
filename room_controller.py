import room
import csv

room_map = {'nest': ['home_door'],
            'library': ['home_door', 'library_door'],
            'east_hall': ['library_door', 'swinging_door', 'servant_door', 'master_door', 'guest_door'],
            'serv_chamber': ['servant_door', 'servant_passage'],
            'gallery': ['gallery_door'],
            'guest_bedroom': ['guest_door'],
            'master_bedroom': ['master_door'],
            'grand_hall': ['swinging_door', 'grand_arch'],
            'living_room': ['grand_arch', 'chapel_door'],
            'chapel': ['chapel_door', 'fsm_door'],
            'west_hall': ['fsm_door', 'kitchen_entry'],
            'kitchen': ['west_hall', 'servant_hall', 'buttery_entry'],
            'servant_hall': ['serv_chamber', 'serv_kitchen'],
            'dresser': ['dresser_drawer'],
            'buttery': ['buttery_entry']
            }

nest = room.Room('nest', 'Home sweet home', room_map['nest'], [])
library = room.Room('library', 'Lots of books', room_map['library'], [])
east_hall = room.Room('east_hall', 'Dark Hallway', room_map['east_hall'], [])
serv_chamber = room.Room('serv_chamber', 'The room for the help', room_map['serv_chamber'], [])
gallery = room.Room('gallery', 'Pretty Art', room_map['gallery'], [])
guest_bedroom = room.Room('guest_bedroom', 'A small room', room_map['guest_bedroom'], [])
master_bedroom = room.Room('master_bedroom', 'A bedroom with a large bed', room_map['master_bedroom'], [])
grand_hall = room.Room('grand_hall', 'A large Atrium', room_map['grand_hall'], [])
living_room = room.Room('living_room', 'Couches and stuff', room_map['living_room'], [])
chapel = room.Room('chapel', 'Flying Spaghetti Monster', room_map['chapel'], [])
west_hall = room.Room('west_hall', 'creeky hallway', room_map['west_hall'], [])
kitchen = room.Room('kitchen', 'There must be cheese somewhere', room_map['kitchen'], [])
servant_hall = room.Room('servant_hall', 'A shortcut', room_map['servant_hall'], [])
dresser = room.Room('dresser', 'Filled with clothes', room_map['dresser'], [])
buttery = room.Room('buttery', 'Filled with cheese', room_map['buttery'], [])

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
buttery_entry = room.Door('butter_entry', 'One more door', kitchen, buttery, True)
serv_kitchen = room.Door('serv_kitchen', 'Servants kitchen entrance', kitchen, servant_hall, False)
servant_passage = room.Door('servant_passage', 'Secret door', serv_chamber, servant_hall, True)
dresser_drawer = room.Door('dresser_drawer', 'A dresser drawer', master_bedroom, dresser, False)



door_dict ={'home_door': home_door,
            'library_door': library_door,
            'swinging_door': swinging_door,
            'servant_door': servant_door,
            'gallery_door': gallery_door,
            'guest_door': guest_door,
            'master_door': master_door,
            'grand_arch': grand_arch,
            'chapel_door': chapel_door,
            'fsm_door': fsm_door,
            'kitchen_entry': kitchen_entry,
            'buttery_entry': buttery_entry,
            'serv_kitchen': serv_kitchen,
            'servant_passage': servant_passage,
            'dresser_drawer': dresser_drawer}

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
current_room = nest
characters = []

while not game_over:
    current_room.look()
    user_input = (input('What is  your command?')).split(' ')
    first = user_input[0]
    second = user_input[1]

    if first == 'open':
        current_room = current_room.open_door(door_dict[second])
    if first == 'look':
        if second == 'room':
            current_room.look()
        if second in current_room.doors:
            print("it is a door")
        if second in current_room.characters:
            print('this is a character')
    if first == 'peek':
        current_room.peek_room(door_dict[second])
