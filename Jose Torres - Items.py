class Items(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Wearable(Items):
    def __init__(self, name, description, wear):
        super(Wearable, self).__init__(name, description)
        self.wear = wear


class Clothes(Wearable):
    def __init__(self, name, description, wear, color):
        super(Clothes, self).__init__(name, description, wear)
        self.color = color


class Shirt(Clothes):
    def __init__(self, name, description, wear, color):
        super(Shirt, self).__init__(name, description, wear, color)

    def wear(self):
        print('You put on the black shirt.')


class Pants(Clothes):
    def __init__(self, name, description, wear, color):
        super(Pants, self).__init__(name, description, wear, color)


class Gloves(Clothes):
    def __init__(self, name, description, wear, color):
        super(Gloves, self).__init__(name, description, wear, color)

    def wear(self):
        print('You put on the Gloves.')


class Shoes(Clothes):
    def __init__(self, name, description, wear, color):
        super(Shoes, self).__init__(name, description, wear, color)

    def wear(self):
        print('You put on the boots.')


class Armor(Wearable):
    def __init__(self, name, description, wear, color):
        super(Armor, self).__init__(name, description, wear,)
        self.color = color


class BulletProofVest(Armor):
    def __init__(self, name, description, wear, color):
        super(BulletProofVest, self).__init__(name, description, wear, color)

    def wear(self):
        print('You put on the BulletProof Vest.')


class MilitaryPants(Armor):
    def __init__(self, name, description, wear, color):
        super(MilitaryPants, self).__init__(name, description, wear, color)

    def wear(self):
        print('You put on the military pants.')


class CombatBoots(Armor):
    def __init__(self, name, description, wear, color):
        super(CombatBoots, self).__init__(name, description, wear, color)

    def wear(self):
        print('You put on the Combat Boots.')


class Consumables(Items):
    def __init__(self, name, description, use):
        super(Consumables, self).__init__(name, description,)
        self.use = use


class Food(Consumables):
    def __init__(self, name, description, use, ):
        super(Food, self).__init__(name, description, use,)


class CarneAsada(Food):
    def __init__(self, name, description, use, eat):
        super(CarneAsada, self).__init__(name, description, use)
        self.eat = eat

    def eat(self):
        print('You ate the Carne Asada.')


class Arroz(Food):
    def __init__(self, name, description, use, eat):
        super(Arroz, self).__init__(name, description, use)
        self.eat = eat

    def eat(self):
        print('You ate the Arroz.')


class Frijoles(Food):
    def __init__(self, name, description, use, eat):
        super(Frijoles, self).__init__(name, description, use)
        self.eat = eat

    def eat(self):
        print('You ate the frijoles.')


class AguaDeHorchata(Food):
    def __init__(self, name, description, use, eat):
        super(AguaDeHorchata, self).__init__(name, description, use,)
        self.eat = eat

    def eat(self):
        print('You drank the Horchata.')


class Medicine(Consumables):
    def __init__(self, name, description, use):
        super(Medicine, self).__init__(name, description, use)


class Ibuprofen(Medicine):
    def __init__(self, name, description, use):
        super(Ibuprofen, self).__init__(name, description, use)

    def use(self):
        print('You took the Ibuprofen')


class Bandages(Medicine):
    def __init__(self, name, description, use):
        super(Bandages, self).__init__(name, description, use)

    def use(self):
        print('You put on the bandage.')


class Weapons(Items):
    def __init__(self, name, description, damage):
        super(Weapons, self).__init__(name, description)
        self.damage = damage


class Melee(Weapons):
    def __init__(self, name, description, damage):
        super(Melee, self).__init__(name, description, damage)


class Sledghammer(Melee):
    def __init__(self, name, description, damage):
        super(Sledghammer, self).__init__(name, description, damage)

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


class LongRange(Weapons):
    def __init__(self, name, description, damage, distance):
        super(LongRange, self).__init__(name, description, damage,)
        self.distance = distance


class ThrowingKnives(LongRange):
    def __init__(self, name, description, damage, distance):
        super(ThrowingKnives, self).__init__(name, description, damage, distance)
        self.distance = distance

    def throw(self):
        print('You threw the knife.')


class Gun(LongRange):
    def __init__(self, name, description, damage, distance):
        super(Gun, self).__init__(name, description, damage, distance)


class AssaultRifle(LongRange):
    def __init__(self, name, description, damage, distance):
        super(AssaultRifle, self).__init__(name, description, damage, distance)

    def shoot(self):
        print('You shoot the assault rifle.')


class Pistol(LongRange):
    def __init__(self, name, description, damage, distance):
        super(Pistol, self).__init__(name, description, damage, distance)
        self.distance = distance

    def shoot(self):
        print('You shot the pistol.')


class Shotgun(LongRange):
    def __init__(self, name, description, damage, distance):
        super(Shotgun, self).__init__(name, description, damage, distance)

    def shoot(self):
        print('You shot the shotgun.')


class KitchenKnife(Melee):
    def __init__(self, name, description, damage):
        super(KitchenKnife, self).__init__(name, description, damage)

    def attack(self):
        print('You swung the knife.')


