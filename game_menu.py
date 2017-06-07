import room_controller
import inventory
import character
import item
import room
import types
#comment
game_over = False

# current_room = room.Room('Test Room', 'This is only a test', test_doors, test_characters)
# next_room = room.Room('next room', 'You have made it to the second room', test_doors, test_characters)
spoon = item.Item('spoon', 'There is no spoon')


# red = room.Door('red', 'A door', current_room, next_room , False, 'no')
# test_doors = [red]
# cat = character.Character('cat', 'Putty Tat', [])
# test_characters = [cat]
def pretty_print_dict(dict):
    for k, v in dict.items():
        print('{}. {}'.format(k, v))


map = item.Item('map', 'You found the map')
current_room = room_controller.nest
current_room.inventory.put_in(spoon)
danger_mouse = character.Mouse('Ralph', 'Test Character', current_room)
danger_mouse.inventory.put_in(map)
while not game_over:
    current_room.look()
    action_select = input('1. Look \n'
                          '2. Move \n'
                          '3. Peek through a door \n'
                          '4. Inventory \n'
                          '5. Interact')

    if action_select == '1':
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

        look_select = input(pretty_print_dict(look_dict))
        look_dict[look_select].look()

    if action_select == '2':
        i = 1
        move_dict = {}
        for door in current_room.doors:
            move_dict[str(i)] = door
            i += 1
        move_select = input(pretty_print_dict(move_dict))
        current_room = current_room.open_door(room_controller.door_dict[move_dict[move_select]])

    if action_select == '3':
        i = 1
        peek_dict = {}
        for door in current_room.doors:
            peek_dict[str(i)] = door
            i += 1
        peek_select = input(pretty_print_dict(peek_dict))
        current_room.peek_room(room_controller.door_dict[peek_dict[peek_select]])

    if action_select == '4':
        inv_dict = danger_mouse.inventory.list_inventory()
        pretty_print_dict(inv_dict)
        item_select = input('Select an item')
        item_action = input('What do you wish to do with this item? \n'
                            '1. Look at item \n'
                            '2. Use item \n'
                            '3. Drop item')
        if item_action == '1':
            inv_dict[item_select].look()
            print('\n')
        if item_action == '2':
            print('You attempt to use the {}, but nothing happens'.format(inv_dict[item_select]))
        if item_action == '3':
            current_room.inventory.put_in(inv_dict[item_select])

    if action_select == '5':
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
        action_item = input('What do you want to interact with?')
        action_dict[action_item].action(current_room, danger_mouse)
