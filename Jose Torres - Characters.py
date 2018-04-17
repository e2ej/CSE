# Must Have:
#     Name
#     Health
#     Pick up Items
#     Move?
#     Attack
#     Death
#     Dialogue
#     Perform Action (Use, Push, etc)
#     Description
#     Status Effect (Paralyze, Poison, Burn, etc)
#     Take Damage


class Characters(object):
    def __init__(self, name, health, attack, description, statuseffect):
        self.name = name
        self.health = health
        self.attack = attack
        self.description = description
        self.statuseffect = statuseffect


THIEF = Characters('Zombie', 10, 'Attack', 'The zombie has a black mask on and the cant see his face.', None)
DOG = Characters('Zombie Dog', 5, 'Attack', 'The dog belongs to the zombie and it attacks you he sees you see you.'
                 , 'fast')