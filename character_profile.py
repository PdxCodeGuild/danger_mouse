"""

"""

import character, item
import room
run_again = True
while run_again == True:

    print("""
        Welcome to the game Danger Mouse!  
        Your goal will be to avoid danger
        while gathering enough food from
        rooms in the castle to last a day.
        
        You will find various spells to 
        aid you.  Keep an eye on your health, 
        as you will need to eat throughout 
        the day and also store food to bring 
        home.  
          
        Please choose a character to play:
        
        1. Mortimer - a wise mouse with a
        keen understanding of the rats
        and dogs who occupy the castle.  
        
        2. Sydney - a clever mouse skilled
        at hiding and evasion from the rats,
        cats, dogs, and people who occupy
        the castle.  
        
        3. Aster - a brave mouse quick to
        cause fright in cats and people
        who occupy the castle.  
        
        """)

    try:
        choice = input("Do you choose character 1, 2, or 3?\n:")
        if choice == '1' or choice == '2' or choice == '3':
            run_again = False

    except:
        continue


if choice == '1':
    befriend_1 = item.Spell('Befriend')
    befriend_2 = item.Spell('Befriend')
    char_list = ['Mortimer', 'You are an elderly mouse who\'s body is worn, but who\'s smile is genuine.', 'library', [befriend_1, befriend_2]]

if choice == '2':
    hide_1 = item.Spell('Hide')
    hide_2 = item.Spell('Hide')
    char_list = ['Sydney', 'You try to look at yourself, but you quickly dodge your own gaze and hide in the shadows.', 'nest', [hide_1, hide_2] ]

if choice == '3':
    scare_1 = item.Spell('Scare')
    scare_2 = item.Spell('Scare')
    char_list = ['Aster', 'Your physical appearance is not notable, but you act with confidence that leaves others intimidated.', 'chapel', [scare_1, scare_2]]

player = character.Mouse(char_list[0], char_list[1], char_list[2])
player.take_item(char_list[3][0])
player.take_item(char_list[3][1])
player.list_inventory()




