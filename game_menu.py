import room_controller
import inventory
import character
import item
import room
game_over = False
spoon = item.Item('spoon', 'There is no spoon')
red = room.Door('red', 'A door', 'front', 'back', False, 'no')
test_doors = [red]
cat = character.Character('cat', 'Putty Tat', [])
test_characters = [cat]
current_room = room.Room('Test Room', 'This is only a test', test_doors, test_characters)
current_room.inventory.put_in(spoon)
while not game_over:
    current_room.look()
    action_select = input('1. Look \n'
                          '2. Move \n'
                          '3. Inventory \n'
                          '4. Interact \n')
    if action_select == '1':
        i = 1
        look_dict ={}
        for door in current_room.doors:
            look_dict[str(i)] = door
            i += 1
        for item in current_room.inventory.bag_of_holding:
            look_dict[str(i)] = item
            i += 1
        for character in current_room.characters:
            look_dict[str(i)] = character
            i += 1

        look_select = input(look_dict)
        look_dict[look_select].look()