class Room(object):
    def __init__(self, name, north, south, east, west, description):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


MYROOM = Room('Your Room', 'SECONDHALL', None, None, None,
              'You are in your room, there is a door north from here.')
SECONDHALL = Room('Second Half of Hallway', 'RESTROOM2', 'MYROOM', 'FIRSTHALL', 'MASTERROOM',
                  'Theres nothing in the '
                  'hallway but a door to the North, West, and East.')
RESTROOM2 = Room('Second Restroom', None, 'SECONDHALL', None, 'MASTERBED',
                 'This is the Second Restroom, there is a '
                 'wrench here. All the cabinets were opened. You can go west or south.')
MASTERROOM = Room('Master Bedroom', 'RESTROOM2', 'GUESTROOM', 'SECONDHALL', None,
                  'The master bedroom is usually clean '
                  'but theres cabinets open and clothes thrown out of the closet. You can go North, East, or South '
                  'from here.')
GUESTROOM = Room('Guest Bedroom', 'MASTERROOM', None, None, None,
                 'The Guest Bedroom is empty but theres a broken '
                 'window and things thrown on the floor. You can go North from here.')
FIRSTHALL = Room('First Half of Hallway', 'RESTROOM1', 'SISTERROOM', 'LIVINGROOM', 'SECONDHALL',
                 'This is the first '
                 'half of the hallway. Pictures on the wall have been moved. You can go West, North, South, or East '
                 'from here.')
RESTROOM1 = Room('First Hallway Restroom', None, 'FIRSTHALL', None, None,
                 'This is the first restroom in the house. '
                 'Theres a broken metal pipe here. There is a door on the South side of the restroom.')
SISTERROOM = Room('Sisters Room', 'FIRSTHALL', None, None, None,
                  'Your in your sisters room but no ones home, theres'
                  ' drawers open in here too. The only way from here is where you came from.')
LIVINGROOM = Room('Living Room', 'KITCHEN', None, 'FRONTYARD', 'FIRSTHALL',
                  'This is the living room, everything is a'
                  ' mess, all the cabinets are open and the couches are moved, the T.V and Xbox are missing too. '
                  'You can go back to the first hallway, North, or East.')
FRONTYARD = Room('Front Yard', None, None, None, 'LIVINGROOM',
                 'The door the the front yard was wide open and theres a'
                 ' weird car parked in the front. You cant find your phone so you cant call your mom, but theres '
                 'someone in your house. You can go West back inside.')
KITCHEN = Room('Kitchen', None, 'LIVINGROOM', 'DININGROOM', None,
               'The refrigerator is gone and theres a meat '
               'tenderizer in the sink. Theres also a hidden key in a jar. You can go East or South from here.')
DININGROOM = Room('Dining Room', 'GARAGE', None, None, 'KITCHEN',
                  'The dining room is empty but the chairs are missing'
                  ' and the table got moved. You can go West or North.')
GARAGE = Room('Garage', None, 'DININGROOM', 'LAUNDRYROOM', 'BACKYARD',
              'All the tools in the garage are gone and they'
              ' are worth a lot of money, theres still a sledgehammer here you can use. You can go South, East, or '
              'West from where you are.')
LAUNDRYROOM = Room('Laundry Room', None, None, None, 'GARAGE',
                   'The laundry room looks like if someone has been in '
                   'here. Theres a paintball gun here and a key for a cabinet. You can only go West from here.')
BACKYARD = Room('Back Yard', None, 'SHED', 'GARAGE', None,
                'The back yard has foot prints on the dirt, the back gate is'
                ' open but you cant leave because you have to take care of the house. Theres a taser gun here. You can '
                'go East or South from here.')
SHED = Room('Shed', 'BACKYARD', None, None, None,
            'The shed is dark and you keep hearing a beeping noise. You hear '
            'people talking but theres no one around. You can only go North out of here.')

current_node = MYROOM
directions = ['north', 'south', 'east', 'west']
short_directions = ['n', 's', 'e', 'w']

while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_').lower().strip()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print('You cannot go this way.')
    else:
        print('Command not recognized.')
