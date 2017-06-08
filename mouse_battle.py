import character_profile
import item
from inventory import Inventory
import character
from random import randrange


# This takes in the player and another character, and then
# it starts a battle. It runs in a while loop. The player
# chooses to fight, use magic, or flee
# {{
def battle(player, npc):
    fighting = True
    print("You are now battling " + npc.name + ". " + npc.description)
    while fighting:
        print("What would you like to do?")
        print("1. Fight")
        print("2. Magic")
        print("3. Flee")
        user_input = input()
        user_input = user_input.lower()


        # This will allow the user to select anything in their inventory,
        # except for a spell. The thing will do damage according to it's
        # attack value (item.attack)
        # It prints damage taken, and then it checks if you've killed
        # the NPC
        # {{
        if "1" in user_input or 'fight' in user_input:

            for thing in danger_mouse.inventory.bag_of_holding:
                if thing.name != "befriend" and thing.name != "hide" and thing.name != "scare":
                    print(thing.name)
            item_select = input('Select an item:\n')
            item_select = item_select.lower()

            for thing in player.inventory.bag_of_holding:
                if thing.name.lower() in item_select:
                    npc.health = npc.health - thing.attack
                    print(npc.name + " took " + str(thing.attack) + ' damage')
                    if npc.health <= 0:
                        print("You have defeated " + npc.name)
                        fighting = False
        # }}


            # npc.take_damage(player.attack)
            # print(npc.name + " took " + str(player.attack) + ' damage')
            # if npc.health <= 0:
            #     print("You have defeated " + npc.name)
            #     fighting = False
        elif '2' in user_input or 'magic' in user_input:
            pass
        elif '3' in user_input or 'flee' in user_input:
            pass




# }}


danger_mouse = character_profile.create_character()
# danger_mouse = character.Mouse('Ralph', 'Test Character', "nest")
current_room = danger_mouse.location
sword = item.Weapon('Sword', 'A dull sword')
danger_mouse.inventory.put_in(sword)
npc_character = character.Cat("Sylvester","He's the family pet, but honestly a pretty feral cat.",current_room )

battle(danger_mouse, npc_character)
