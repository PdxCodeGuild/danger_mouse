import room_controller
import inventory
import character
import item
import room
import types
game_over = False

# current_room = room.Room('Test Room', 'This is only a test', test_doors, test_characters)
# next_room = room.Room('next room', 'You have made it to the second room', test_doors, test_characters)
spoon = item.Item('spoon', 'There is no spoon')

baby_mouse = character.Character('baby', 'little rodent', room_controller.nest,)
# red = room.Door('red', 'A door', current_room, next_room , False, 'no')
# test_doors = [red]
# cat = character.Character('cat', 'Putty Tat', [])
# test_characters = [cat]
def pretty_print_dict(dict):
    for k in dict:
        print('{}. {}'.format(k, dict[k]))


map = item.Item('map', 'You found the map')
current_room = room_controller.nest
current_room.inventory.put_in(spoon)
current_room.characters.append(baby_mouse)
danger_mouse = character.Mouse('Ralph', 'Test Character', current_room)
danger_mouse.inventory.put_in(map)
print("You are a 🐭")
while not game_over:
    current_room.look()
    action_select = str(input('1. Look \n'
                          '2. Move \n'
                          '3. Peek through a door \n'
                          '4. Inventory \n'
                          '5. Interact\n')).lower()

    if '1' in action_select or 'look' in action_select:
        i = 1
        look_dict = {}
        for door in current_room.doors:
            look_dict[str(i)] = room_controller.door_dict[door]
            i += 1
        for item in current_room.inventory.bag_of_holding:
            look_dict[str(i)] = item
            i += 1
        for character in current_room.characters:
            look_dict[str(i)] = character
            i += 1
        valid_input = False
        while not valid_input:
            try:
                pretty_print_dict(look_dict)
                look_select = input('What do you want to look at?')
                look_dict[look_select].look()
                valid_input = True
            except KeyError:
                print("Not a valid input")

    elif '2' in action_select or 'move' in action_select:
        i = 1
        move_dict = {}
        for door in current_room.doors:
            move_dict[str(i)] = door
            i += 1
        valid_input = False
        while not valid_input:
                try:
                    for k in move_dict:
                        print(k + '. ' + move_dict[k])
                    move_select = input()
                    current_room = current_room.open_door(room_controller.door_dict[move_dict[move_select]])
                    valid_input = True
                except KeyError:
                    print("Not a valid input")

    elif '3' in action_select or 'peek' in action_select:
        i = 1
        peek_dict = {}
        for door in current_room.doors:
            peek_dict[str(i)] = door
            i += 1

        valid_input = False
        while not valid_input:
                try:
                    for k in peek_dict:
                        print(k + '. ' + peek_dict[k])
                    peek_select = input()
                    current_room.peek_room(room_controller.door_dict[peek_dict[peek_select]])
                    valid_input = True
                except KeyError:
                    print("Not a valid input")

    elif '4' in action_select or 'inventory' in action_select:
        inv_dict = danger_mouse.inventory.list_inventory()
        pretty_print_dict(inv_dict)
        item_select = input('Select an item')
        item_action = input('What do you wish to do with this item? \n'
                            '1. Look at item \n'
                            '2. Use item \n'
                            '3. Drop item\n')

        if '1' in item_action:
            inv_dict[item_select].look()
            print('\n')
        if '2' in item_action:
            print('You attempt to use the {}, but nothing happens'.format(inv_dict[item_select]))
        if '3' in item_action:
            current_room.inventory.put_in(danger_mouse.inventory.poplar(inv_dict[item_select]))

    elif '5' in action_select or 'interact' in action_select:
        action_dict = {}
        i = 1
        for door in current_room.doors:
            action_dict[str(i)] = room_controller.door_dict[door]
            i += 1
        for item in current_room.inventory.bag_of_holding:
            action_dict[str(i)] = item
            i += 1
        for character in current_room.characters:
            action_dict[str(i)] = character
            i += 1
        pretty_print_dict(action_dict)
        action_item = input('What do you want to interact with?\n')
        action_dict[action_item].action(current_room, danger_mouse)

    else:
        print('Please enter a valid menu option.')
