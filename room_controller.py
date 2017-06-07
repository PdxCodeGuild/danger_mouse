import room
import csv
import character
from character import Mouse

room_map = {'nest': ['mouse_hole'],
            'library': ['mouse_hole', 'library_door'],
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
            'buttery': ['buttery_entry'],
            'front_lawn':['front_door']
            }


# Room initializations
# name, description, doors[], characters[]
nest = room.Room('nest', "You are in your mouse nest, in a large castle. The belongings in the nest are yours and you recognize all of them. You see your mouse family, hungry and waiting patiently for you to bring home enough food for everyone to eat.", room_map['nest'], [])
library = room.Room('library', 'You are in the library. It once occured to you to read them all, but a mouse like you need not concern itself with such things.', room_map['library'], [])
east_hall = room.Room('east_hall', "You are in the east hallway, it's very dark in here. You look around for light leaking under doorways to find your exits.", room_map['east_hall'], [])
serv_chamber = room.Room('serv_chamber', "The room for the help. They sneak your family cheese sometimes, but they appear busy today.", room_map['serv_chamber'], [])
gallery = room.Room('gallery', "You enter the castle art gallery. Its most prized pieces include paintings by Monet, however you've always been more of a Dali fan yourself.", room_map['gallery'], [])
guest_bedroom = room.Room('guest_bedroom', "The guest bedroom. You tried to sleep in there once but APPARENTLY don't qualify as a guest.", room_map['guest_bedroom'], [])
master_bedroom = room.Room('master_bedroom', "The master bedroom. Not a bedroom for the common mouse.", room_map['master_bedroom'], [])
grand_hall = room.Room('grand_hall', "You enter the grand entry hall. It's pillars and golden statues boast of a life lived in luxury, a red cloth banner on the ceiling reads \"There are no god's or kings, only men.\"", room_map['grand_hall'], [])
living_room = room.Room('living_room', "You enter the livingroom. Mostly just for show and guests, otherwise the room is rarely used.", room_map['living_room'], [])
chapel = room.Room('chapel', "You enter the Chapel room. However Dave doesn't appear to be here at the moment 'man'.", room_map['chapel'], [])
west_hall = room.Room('west_hall', "This is the western hallway. The windows allow the sun to illuminate the hall with its shining brilliance, much better hallway than that other one.", room_map['west_hall'], [])
kitchen = room.Room('kitchen', "Kitchen, there must be cheese somewhere.", room_map['kitchen'], [])
servant_hall = room.Room('servant_hall', "The servants hall. You can't just have your servants walking around the castle like they own the place, right?", room_map['servant_hall'], [])
dresser = room.Room('dresser', "You find yourself in a dresser, and much to your own surprise it's filled with clothes! You make a note to come back during winter.", room_map['dresser'], [])
buttery = room.Room('buttery', "The buttery, there's wine and cheese everywhere!", room_map['buttery'], [])
outside = room.Room('front_lawn', "You are on the front lawn. You peer upward towards the sky, into the void of infinity. It's a great big universe and you're just a small part of it. The sheer impact of this realization, of having grasped the nature of the cosmos and the universe has unfortunately so blown your mind that it has left you comatose, your family will surely perish. Game Over.",room_map['front_lawn'],[])

# Door initializations
# name, description, room1, room2, is_locked, key_name
mouse_hole = room.Door('mouse_hole', 'A hole in the baseboard of the castle library, the entry way to your humble home.', nest, library, False, 'mouse_hole_key')
library_door = room.Door('library_door', 'A crack under the door', library, east_hall, False, 'library_door_key')
swinging_door = room.Door('swinging_door', 'A swinging door', east_hall, grand_hall, False, 'swinging_door_key')
servant_door = room.Door('servant_door', 'A wooden door', east_hall, serv_chamber, True, 'servant_door_key')
gallery_door = room.Door('gallery_door', 'It looks like you can squeze through the door', east_hall, gallery, False, 'gallery_door_key')
guest_door = room.Door('guest_door', 'A wooden door', east_hall, guest_bedroom, False, 'guest_door_key')
master_door = room.Door('master_door', 'A wooden door', east_hall, master_bedroom, True, 'master_door_key')
grand_arch = room.Door('grand_arch', 'A large archway', grand_hall, living_room, False, 'grand_arch_key')
chapel_door = room.Door('chapel_door', 'A thick door', living_room, chapel, False, 'chapel_door_key')
fsm_door = room.Door('fsm_door', 'The flying speghetti monster rests on the door', chapel, west_hall, False, 'fsm_door_key')
kitchen_entry = room.Door('kitchen_entry', 'A swinging double door', west_hall, kitchen, False, 'kitchen_door_key')
buttery_entry = room.Door('butter_entry', 'One more door', kitchen, buttery, True, 'buttery_door_key')
serv_kitchen = room.Door('serv_kitchen', 'Servants kitchen entrance', kitchen, servant_hall, False, 'serv_door_key')
servant_passage = room.Door('servant_passage', 'Secret door', serv_chamber, servant_hall, True, 'servant_passage_key')
dresser_drawer = room.Door('dresser_drawer', 'A dresser drawer', master_bedroom, dresser, False, 'dresser_drawer_key')
front_door = room.Door('front_door', 'The front entrance to the castle, really quite a beautiful doorway, not that the opinion of a mouse matters.',grand_hall, outside, False, 'front_door_key' )


door_dict ={'mouse_hole': mouse_hole,
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


# when passed a list of all the characters and rooms, will sort through them and update the locations on each accordingly
def update_all(characters, castle):
    for loc in castle:
        temp_list = []
        for person in characters:
            if person.location == loc.name:
                temp_list.append(person)
        loc.update_characters(temp_list)







# game_over = False
# current_room = nest
# characters = []
# player = Mouse('Mouse', 'Looks like a mouse', current_room)
# while not game_over:
#     failed_door_open = ''
#     current_room.surroundings()
#     user_input = (input('What is  your command?'))
#     user_input = user_input.lower()
#
#
#     if 'open' in user_input:
#         for door in current_room.doors:
#             if door in user_input:
#                 current_room = current_room.open_door(door_dict[door])
#                 break
#
#     if 'use' in user_input:
#         for thing in user_input:
#             if 'key' in thing:
#                 for door in current_room.doors:
#                     if door.name in user_input:
#                         current_room.use_key(door, player)



    # if first == 'open':
    #     current_room = current_room.open_door(door_dict[second])
    # if first == 'look':
    #     if second == 'room':
    #         current_room.look()
    #     if second in current_room.doors:
    #         print("it is a door")
    #     if second in current_room.characters:
    #         print('this is a character')
    # if first == 'peek':
    #     current_room.peek_room(door_dict[second])
