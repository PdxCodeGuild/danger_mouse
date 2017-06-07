
while True:
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
        player = input("Please choose your mouse: ")

    except:
        ValueError
        continue




