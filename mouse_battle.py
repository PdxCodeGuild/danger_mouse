import character_profile
import item
from inventory import Inventory
import character
from random import randrange

def pretty_print_dict(dict):
    for k in dict:
        print('{}. {}'.format(k, dict[k]))

def battle(player, npc):
    fighting = True
    print("You are now battling " + npc.name + ". " + npc.description)
    while fighting:
        print("What would you like to do?")
        print("1. Attack")
        print("2. Magic")
        print("3. Flee")
        user_input = input()
        user_input = user_input.lower()

        if "1" in user_input or 'fight' in user_input:
            inv_dict = danger_mouse.inventory.list_inventory()
            pretty_print_dict(inv_dict)
            item_select = input('Select an item')
            item_select = item_select.lower()
            
            for thing in player.inventory.bag_of_holding:
                if thing.name.lower() in item_select:
                    npc.health = npc.health - thing.attack
                    print(npc.name + " took " + str(player.attack) + ' damage')
                    if npc.health <= 0:
                        print("You have defeated " + npc.name)
                        fighting = False

            # npc.take_damage(player.attack)
            # print(npc.name + " took " + str(player.attack) + ' damage')
            # if npc.health <= 0:
            #     print("You have defeated " + npc.name)
            #     fighting = False
        elif '2' in user_input or 'magic' in user_input:
            pass
        elif '3' in user_input or 'flee' in user_input:
            pass





# danger_mouse = character_profile.create_character()
danger_mouse = character.Mouse('Ralph', 'Test Character', "nest")
current_room = danger_mouse.location
sword = item.Weapon('Sword', 'A dull sword')
danger_mouse.inventory.put_in(sword)
npc_character = character.Cat("Sylvester","He's the family pet, but honestly a pretty feral cat.",current_room )

battle(danger_mouse, npc_character)
