import room
room_map = dict{'nest': ['library']
                'library': ['east_hall', 'nest'],
                'east_hall': ['library', 'serv_camber', 'gallery', 'guest_bedroom', 'master_bedroom', 'main_hall'],
                'serv_chamber': ['east_hall', 'servant_hall'],
                'gallery': ['east_hall'],
                'guest_bedroom': ['east_hall'],
                'master_bedroom': ['east_hall', 'chest_one'],
                'main_hall': ['east_hall', 'living_room', 'outside'],
                'living_room': ['main_hall', 'chapel'],
                'chapel': ['living_room', 'west_hall'],
                'west_hall': ['chapel', 'kitchen'],
                'kitchen': ['west_hall', 'buttery', 'servant_hall'],
                'servant_hall': ['serv_chamber', 'kitchen']
                }



