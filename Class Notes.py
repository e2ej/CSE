# Defining a Class
class CheeseBurger(object):
    def __init__(self, patty_type, cheese):  # TWO Underscores Before and After
        self.patty = patty_type
        self.cheese = cheese
        self.eaten = False

    def give(self, name):
        print(name + 'is thankful.')

    def cut(self):
        print('You cut the cheeseburger.')

    def eat(self):
        print('You eat the cheeseburger.')
        self.eaten = True


# Initializing (The Creation of) Two CheeseBurgers
burger1 = CheeseBurger('Beef', 'Swiss')
burger2 = CheeseBurger('Bacon', "Havarti")

print(burger1.eaten)
print(burger2.cheese)

burger1.eat()
print(burger1.eaten)
print(burger2.eaten)


class car(object):
    def __init__(self, name, color, num_of_doors, hp):
        self.color = color
        self.doors = num_of_doors
        self.running = False
        self.HP = hp
        self.passengers = 0
        self.name = name
        self.air_conditioning = True

    def turn_on(self):
        if self.running:
            print('Nothing Happens.')
        else:
            self.running = True
            print('The Car Starts.')

    def move_forward(self):
        if self.running:
            print('You Moved Forward.')
        else:
            print('Nothing Happens.')

    def turn_off(self):
        if self.running:
            self.running = False
            print('You Turn Off The Car.')
        else:
            print('The Car Is Already Off.')

    def go_for_drive(self, passengers):
        print('%d passengers get in' % passengers)
        self.passengers = passengers
        self.turn_on()
        self.move_forward()
        self.move_forward()
        self.move_forward()
        self.turn_off()
        print('%d passengers get off.' % passengers)
        self.passengers = 0


my_car = car('Nissan GTR', 'Chrome', 2, 580)

car2 = car('Lamborghini Aventador', 'Red', 2, 730)

