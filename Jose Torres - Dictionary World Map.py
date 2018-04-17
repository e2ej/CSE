world_map = {
    'MYROOM': {
        'NAME': 'Your Room',
        'DESCRIPTION': 'You are in your room. There is a door on the North of the room.',
        'PATHS': {
            "NORTH": 'SECONDHALL'
        }
    }, "SECONDHALL": {
        'NAME': 'Second Half of Hallway',
        'DESCRIPTION': 'Theres nothing in the hallway but a door to the North, West, and East.',
        'PATHS': {
            'WEST': 'MASTERROOM',
            'NORTH': 'RESTROOM2',
            'EAST': 'FIRSTHALL',
            'SOUTH': 'MYROOM'
        }
    }, "RESTROOM2": {
        "NAME": 'Second Restroom',
        'DESCRIPTION': 'This is the Second Restroom there is a wrench in here and cabinets are open. From here you can '
                       'go'
                       ' West'
                'or South',
        'PATHS': {
            'WEST': 'MASTERROOM',
            'SOUTH': 'SECONDHALL'
        }
    }, "MASTERROOM": {
        'NAME': 'Master Bedroom',
        'DESCRIPTION': 'The master bedroom is usually clean but theres cabinets open and clothes thrown out of the'
                       'closet. You can go North, East, or South from here.',
        'PATHS': {
            'NORTH': 'RESTROOM2',
            'EAST': 'SECONDHALL',
            'SOUTH': 'GUESTROOM'
        }
    }, "GUESTROOM": {
        'NAME': 'Guest Bedroom',
        'DESCRIPTION': 'The Guest Bedroom is empty but theres a broken window and things thrown on the floor. You can'
                       ' go North from here.',
        'PATHS': {
            'NORTH': 'MASTERROOM'
        }
    }, "FIRSTHALL": {
        'NAME': 'First Half of Hallway',
        'DESCRIPTION': 'This is the first half of the hallway. Pictures on the wall have been moved. You can go West,'
                       'North, South, or East from here.',
        'PATHS': {
            'NORTH': 'RESTROOM1',
            'WEST': 'SECONDHALL',
            'SOUTH': 'SISTERROOM',
            'EAST': 'LIVINGROOM'
        }
    }, 'RESTROOM1': {
        'NAME': 'Second Restroom',
        'DESCRIPTION': 'This is the second restroom in the house. Theres a broken metal pipe here. There is a door on'
                       'South side of the restroom.',
        'PATHS': {
            'SOUTH': 'FIRSTHALL'
        }
    }, "SISTERROOM": {
        'NAME': 'Sisters Room',
        'DESCRIPTION': 'Your in your sisters room but no ones home, theres drawers open in here too. The only way from'
                       'here is where you came from.',
        'PATHS': {
            'NORTH': 'FIRSTHALL'
        }
    }, "LIVINGROOM": {
        'NAME': 'Living Room',
        'DESCRIPTION': 'This is the living room, everything is a mess, all the cabinets are open and the couches are'
                       'moved, the T.V and Xbox are missing too. You can go back to the first hallway, North, or East.',
        'PATHS': {
            'WEST': 'FIRSTHALL',
            'NORTH': 'KITCHEN',
            'EAST': 'FRONTYARD'
        }
    }, "FRONTYARD": {
        'NAME': 'Front Yard',
        'DESCRIPTION': 'The door the the front yard was wide open and theres a weird car parked in the front. You cant'
                       'find your phone so you cant call your mom, but theres someone in your house. You can go West'
                       'back inside.',
        'PATHS': {
            'WEST': 'LIVINGROOM'
        }
    }, "KITCHEN": {
        'NAME': 'Kitchen',
        'DESCRIPTION': 'The refrigerator is gone and theres a meat tenderizer in the sink. Theres also a hidden key in'
                       'a jar. You can go East or South from here.',
        'PATHS': {
            'SOUTH': 'LIVINGROOM',
            'EAST': 'DININGROOM'
        }
    }, "DININGROOM": {
        "NAME": 'Dining Room',
        'DESCRIPTION': 'The dining room is empty but the chairs are missing and the table got moved. You can go West or'
                       'North.',
        'PATHS': {
            'WEST': 'KITCHEN',
            'NORTH': 'GARAGE'
        }
    }, "GARAGE": {
        'NAME': 'Garage',
        'DESCRIPTION': 'All the tools in the garage are gone and they are worth alot of money, theres still a'
                       ' sledgehammer here you can use. You can go South, East, or West from where you are.',
        'PATHS': {
            'WEST': 'BACKYARD',
            'SOUTH': 'DININGROOM',
            'EAST': 'LAUNDRYROOM'
        }
    }, "LAUNDRYROOM": {
        'NAME': 'Laundry Room',
        'DESCRIPTION': 'The laundry room looks like if someone has been in here. Theres a paintball gun here and a key'
                       ' for a cabinet. You can only go West from here.',
        'PATHS': {
            'WEST': 'GARAGE'
        }
    }, "BACKYARD": {
        'NAME': 'Back Yard',
        'DESCRIPTION': 'The back yard has foot prints on the dirt, the back gate is open but you cant leave because you'
                       'have to take care of the house. Theres a taser gun here. You can go East or South from here.',
        'PATHS': {
            'EAST': 'GARAGE',
            'SOUTH': 'SHED'
        }
    }, 'SHED': {
        'NAME': 'Shed',
        'DESCRIPTION': 'The shed is dark and you keep hearing a beeping noise. You hear people talking but theres no'
                       ' one around. You can only go North out of here.',
        'PATHS': {
            'NORTH': 'BACKYARD'
        }
    }

}

current_node = world_map['MYROOM']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST']

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = world_map[name_of_node]
        except KeyError:
            print('You cannot go this way.')
    else:
        print('Command not recognized.')
