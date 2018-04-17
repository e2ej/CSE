class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Wearable(Item):
    def __init__(self, name, description, wear):
        super(Wearable, self).__init__(name, description)
        self.wear = wear


class Clothes(Wearable):
    def __init__(self, name, description, color):
        super(Clothes, self).__init__(name, description, color)
        self.color = color


class Shirt(Clothes):
    def __init__(self, name, description, color):
        super(Shirt, self).__init__(name, description, color)


class Pants(Clothes):
    def __init__(self, name, description, color):
        super(Pants, self).__init__(name, description, color)


class Gloves(Clothes):
    def __init__(self, name, description, color):
        super(Gloves, self).__init__(name, description, color)


class Shoes(Clothes):
    def __init__(self, name, description, color):
        super(Shoes, self).__init__(name, description, color)


class Armor(Wearable):
    def __init__(self, name, description, color):
        super(Armor, self).__init__(name, description, color)
        self.color = color


class BulletProofVest(Armor):
    def __init__(self, name, description, color):
        super(BulletProofVest, self).__init__(name, description, color)


class MilitaryPants(Armor):
    def __init__(self, name, description, color):
        super(MilitaryPants, self).__init__(name, description, color)


class CombatBoots(Armor):
    def __init__(self, name, description, color):
        super(CombatBoots, self).__init__(name, description, color)


class Consumable(Item):
    def __init__(self, name, description, use):
        super(Consumable, self).__init__(name, description, )
        self.use = use


class Food(Consumable):
    def __init__(self, name, description, use, ):
        super(Food, self).__init__(name, description, use,)


class CarneAsada(Food):
    def __init__(self, name, description, use, eat):
        super(CarneAsada, self).__init__(name, description, use)
        self.eat = eat

    def eat(self):
        print('You ate the Carne Asada.')


class PlateOfArroz(Food):
    def __init__(self, name, description, use, eat):
        super(PlateOfArroz, self).__init__(name, description, use)
        self.eat = eat

    def eat(self):
        print('You ate the Arroz.')


class PlateofFrijoles(Food):
    def __init__(self, name, description, use, eat):
        super(PlateofFrijoles, self).__init__(name, description, use)
        self.eat = eat

    def eat(self):
        print('You ate the frijoles.')


class VasoDeAguaDeHorchata(Food):
    def __init__(self, name, description, use, eat):
        super(VasoDeAguaDeHorchata, self).__init__(name, description, use, )
        self.eat = eat

    def eat(self):
        print('You drank the Horchata.')


class Medicine(Consumable):
    def __init__(self, name, description, use):
        super(Medicine, self).__init__(name, description, use)


class Ibuprofen(Medicine):
    def __init__(self, name, description, use):
        super(Ibuprofen, self).__init__(name, description, use)

    def use(self):
        print('You took the Ibuprofen')


class Bandage(Medicine):
    def __init__(self, name, description, use):
        super(Bandage, self).__init__(name, description, use)

    def use(self):
        print('You put on the bandage.')


class Weapon(Item):
    def __init__(self, name, description, damage):
        super(Weapon, self).__init__(name, description)
        self.damage = damage


class Melee(Weapon):
    def __init__(self, name, description, damage):
        super(Melee, self).__init__(name, description, damage)


class Sledgehammer(Melee):
    def __init__(self, name, description, damage):
        super(Sledgehammer, self).__init__(name, description, damage)

    def attack(self):
        print('You swung the hammer.')


class Wrench(Melee):
    def __init__(self, name, description, damage):
        super(Wrench, self).__init__(name, description, damage)

    def attack(self):
        print('You swung with the wrench.')


class BrokenMetalPipe(Melee):
    def __init__(self, name, description, damage):
        super(BrokenMetalPipe, self).__init__(name, description, damage)

    def attack(self):
        print('You swing the metal pipe.')


class LongRange(Weapon):
    def __init__(self, name, description, damage, accuracy):
        super(LongRange, self).__init__(name, description, damage,)
        self.distance = accuracy


class ThrowingKnife(LongRange):
    def __init__(self, name, description, damage, accuracy):
        super(ThrowingKnife, self).__init__(name, description, damage, accuracy)
        self.distance = accuracy

    def throw(self):
        print('You threw the knife.')


class PaintballGun(LongRange):
    def __init__(self, name, description, damage, accuracy):
        super(PaintballGun, self).__init__(name, description, damage, accuracy)


class AssaultRifle(LongRange):
    def __init__(self, name, description, damage, accuracy):
        super(AssaultRifle, self).__init__(name, description, damage, accuracy)

    def shoot(self):
        print('You shoot the assault rifle.')


class Pistol(LongRange):
    def __init__(self, name, description, damage, accuracy):
        super(Pistol, self).__init__(name, description, damage, accuracy)
        self.distance = accuracy

    def shoot(self):
        print('You shot the pistol.')


class Shotgun(LongRange):
    def __init__(self, name, description, damage, accuracy):
        super(Shotgun, self).__init__(name, description, damage, accuracy)

    def shoot(self):
        print('You shot the shotgun.')


class KitchenKnife(Melee):
    def __init__(self, name, description, damage):
        super(KitchenKnife, self).__init__(name, description, damage)

    def attack(self):
        print('You swung the knife.')


class Characters(object):
    def __init__(self, name, health, attack, description, statuseffect):
        self.name = name
        self.health = health
        self.attack = attack
        self.description = description
        self.statuseffect = statuseffect


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


ITEMS = Item('Items', 'Items')
SHIRT = Shirt('Shirts', 'Wearable Shirt', 'Black')
PANTS = Pants('Pants', 'Wearable Pants', 'Navy Blue')
GLOVES = Gloves('Gloves', 'Wearable Gloves', 'Black')
SHOES = Shoes('Shoes', 'Pair of Shoes.', 'Black')
BULLETPROOFVEST = BulletProofVest('Bullet Proof Vest', 'A bullet proof vest, can probably take a slug shot.', 'Grey')
COMBATBOOTS = CombatBoots('Combat Boots', 'Can break a skull if you try hard enough.', 'Black')
CARNEASADA = CarneAsada('Carne Asada', 'Really good in tacos.', None, True)
PLATEOFARROZ = PlateOfArroz('Plate of Arroz', 'Its a plate of rice.', None, True)
PLATEOFFRIJOLES = PlateofFrijoles('Plate of Frijoles', 'Its a plate of beans.', None, True)
VASODEAGUADEHORCHATA = VasoDeAguaDeHorchata('Vaso de Agua de Horchata', 'Its a cup of Horchata', None, True)
IBUPROFEN = Ibuprofen('Ibuprofen', 'It helps if your hurt, just take the whole bottle.', True)
BANDAGE = Bandage('Bandage', 'It has spider-man on it but it helps if your hurt.', True)
SLEDGEHAMMER = Sledgehammer('Sledgehammer', 'Could break bones if you try hard enough.', 7)
WRENCH = Wrench('Wrench', 'Used to fix cars but could do some damage.', 5)
BROKENMETALPIPE = BrokenMetalPipe('Broken Metal Pipe', 'Cant do much but it can hurt when you hit someone with it.', 2)
KITCHENKNIFE = KitchenKnife('Kitchen Knife', 'Its used to cut meat so it will do good.', 8)
THROWINGKNIFE = ThrowingKnife('Throwing Knife', 'Could do damage if you know how to throw it.', 10, 5)
PAINTBALLGUN = PaintballGun('Paintball Gun', 'Shoots paint balls pretty far.', 2, 7)
ASSAULTRIFLE = AssaultRifle('Assault Rifle', 'It shoots fast but accuracy is kinda bad.', 10, 5)
PISTOL = Pistol('Pistol', 'Pretty good accuracy but less damage.', 6, 8)
SHOTGUN = Shotgun('Shotgun', 'Really bad accuracy but really good damage.', 10, 3)


ZOMBIE = Characters('Zombie', 10, 'Attack', 'The zombie has a black mask on and the cant see his face.', None)
DOG = Characters('Zombie Dog', 5, 'Attack', 'The dog belongs to the zombie and it attacks you when it sees you.',
                 'fast')


MYROOM = Room('Your Room', 'SECONDHALL', None, None, None,
              'You are in your room, there is a door north from here.')
SECONDHALL = Room('Second Half of Hallway', 'RESTROOM2', 'MYROOM', 'FIRSTHALL', 'MASTERROOM',
                  'Theres nothing in the '
                  'hallway but a door to the North, West, and East.')
RESTROOM2 = Room('Second Restroom', None, 'SECONDHALL', None, 'MASTERBED',
                 'This is the Second Restroom. All the cabinets were opened. You can go west or south.')
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
                 'This is the first restroom in the house. There is a door on the South side of the restroom.')
SISTERROOM = Room('Sisters Room', 'FIRSTHALL', None, None, None,
                  'Your in your sisters room but no ones home, theres'
                  ' drawers open in here too. The only way from here is where you came from.')
LIVINGROOM = Room('Living Room', 'KITCHEN', None, 'FRONTYARD', 'FIRSTHALL',
                  'This is the living room, everything is a'
                  ' mess, all the cabinets are open and the couches are moved, the T.V and Xbox are missing too. '
                  'You can go back to the first hallway, North, or East.')
FRONTYARD = Room('Front Yard', None, None, None, 'LIVINGROOM',
                 'The door the the front yard was wide open and theres a'
                 ' gate that leads to a helicopter. You cant find your phone so you cant call your mom, but theres '
                 'someone in your house. You can go West back inside.')
KITCHEN = Room('Kitchen', None, 'LIVINGROOM', 'DININGROOM', None,
               'The refrigerator is gone and theres a meat. Theres also a hidden key in a jar. You can go East or'
               ' South from here.')
DININGROOM = Room('Dining Room', 'GARAGE', None, None, 'KITCHEN',
                  'The dining room is empty but the chairs are missing'
                  ' and the table got moved. You can go West or North.')
GARAGE = Room('Garage', None, 'DININGROOM', 'LAUNDRYROOM', 'BACKYARD',
              'All the tools in the garage are gone and they are worth a lot of money. You can go South, East, or '
              'West from where you are.')
LAUNDRYROOM = Room('Laundry Room', None, None, None, 'GARAGE',
                   'The laundry room looks like if someone has been in '
                   'here. Theres a key for a cabinet. You can only go West from here.')
BACKYARD = Room('Back Yard', None, 'SHED', 'GARAGE', None,
                'The back yard has foot prints on the dirt, the back gate is'
                ' open but you cant leave because you have to take care of the house. Theres a taser gun here. You can '
                'go East or South from here.')
SHED = Room('Shed', 'BACKYARD', None, None, None,
            'The shed is dark and almost everything is gone. You hear '
            'a dog barking but theres no one around. You can only go North out of here.')


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
