'''
# print("Hello World")
#
# # Jose Torres
#
# a = 4
# b = 3
#
# print(3 + 5)
# print(5 - 3)
# print(3 * 5)
# print(3 + 5)
# print(3 ** 2)
#
# print()
# print("Try to find out how this works")
# print(15 % 5)
#
# # the "%" sign is a modulus. It finds the remainder.
#
# car_name = "The Wiebe Mobile"
# car_type = "BMW"
# car_cylinders = 8
# car_mpg = 5000.9
#
# print("I have a car called %s. It's pretty nice." % car_name)
# print("I have a car called %s. It's a %s." % (car_name, car_type))  # watch the order
#
# # Here is where we get a little fancy
# print("What is your name?")
# name = input(">_")
#
# print("Hello %s" % name)
# age = input("How old are you?")
#
# print("%s?! That's really old. You belong in a retirement home." % age)

# Functions
# Indent has to have four spaces or code won't run.

def print_hw():
    print("Hello World.")
    print("Enjoy the Day")


print_hw()


def say_hi(name):  # Name is a "Parameter"
    print("Hello %s" % name)
    print("Coding is great!")


say_hi("John")


def print_age(name, age):
    print("%s is %s years old" % (name, age))
    age = age + 1  # age = age + 1
    print("Next year, %s will be %d years old" % (name, age))


print_age("John", 15)


def algebra_hw(x):
    return x**3 + 4*x**2 + 7 * x - 4


print(algebra_hw(3))
print(algebra_hw(4))
print(algebra_hw(5))
print(algebra_hw(6))
print(algebra_hw(7))


# if statements


def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:  # else if
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


print(grade_calc(59))


def happy_bday(name):
    print("Happy Birthday to you")
    print("Happy Birthday to you")
    print("Happy Birthday dear %s" % name)
    print("Happy Birthday to you")

# Loops

for num in range (10):
    print(num + 1)

# White loops (BEWARRRRRRE!!!)

a = 1
while a < 10:  #this is the condition, it must be true,
               #to execute
    print(a)
    a += 1  # This literates so we can break the loop


# Random Numbers
import random # this should be on line 1
print(random.randint(0, 1000))

# lists

the_count = [1, 2, 3, 4, 5]
cheeseburger_ingredients = ['cheese', "beef", 'sauce', 'sesame seed buns', 'grilled onions', 'bacon']
print(cheeseburger_ingredients[0])
print(cheeseburger_ingredients[3])
print(len(cheeseburger_ingredients))

# Going through lists
for generic_item_name in cheeseburger_ingredients:
    print(generic_item_name)

for num in the_count:
    print(num * 2)

length = len(cheeseburger_ingredients)
range(5)  # A list of the numbers 0 through 4
range(len(cheeseburger_ingredients))  # Generates a list of all indices

for num in range(len(cheeseburger_ingredients)):
    item = cheeseburger_ingredients[num]
    print("The item at index %d is %s" % (num, item))

# Recasting into a list
strOne = "Hello World!"
listOne = list(strOne)
print(listOne)
listOne[11] = '.'
print(listOne)
print(listOne[-1])

# Adding things to a list
cheeseburger_ingredients.append("Fries")
cheeseburger_ingredients.append("Soda")
print(cheeseburger_ingredients)

# Remove things from a list
cheeseburger_ingredients.pop(1)
print(cheeseburger_ingredients)
cheeseburger_ingredients.remove("cheese")
print(cheeseburger_ingredients)

# Getting the alphabet
import string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.punctuation)

# Making things Lowercase
strTwo = "ThIs iS A veRy oDd SenTEnCe"
lowercase = strTwo.lower()
print(lowercase)

# l1 = ['h','e','l','l','o']
# "". join(l1)
'''

# Dictionaries - Made up of key value pair

dictionary = {"name": 'Lance', 'age': 26, 'height': 6 * 12 + 2}

# Accessing things from a dictionary
print(dictionary['name'])
print(dictionary['age'])
print(dictionary["height"])

# Add a pair to a dictionary
dictionary["profession"] = "telemarketer"

large_dictionary = {
    'CA': 'California',
    'AZ': 'Arizona',
    'NY': 'New York'
}
print(large_dictionary["NY"])

larger_dictionary = {
    'CA': [
        'Fresno',
        'San Francisco',
        'San Jose'
    ],
    'AZ': [
        'Phoenix',
        'Tuscon'
    ],
    'NY': [
        'New York City',
        'Brooklyn'
    ]
}

print(larger_dictionary['NY'])
print(larger_dictionary["AZ"][0])

largest_dictionary = {
    'CA': {
        'NAME': "California",
        'POPULATION': 39250000,
        'BORDER ST': [
            'Oregon',
            'Nevada',
            'Arizona'
        ]
    },
    'AZ': {
        'NAME': 'Arizona',
        'POPULATION': 6931000,
        'BORDER ST': [
            'California',
            'Nevada',
            'New Mexico'
        ]
    },
    'NY': {
        'NAME': 'New York',
        'POPULATION': 19750000,
        'BORDER ST': [
            'Vermont',
            'Massachusetts',
            'Connecticut',
            'Pennsylvania',
            'New Jersey'
        ]
    },
}

current_node = largest_dictionary['NY']
print(current_node['BORDER ST'][1])
print(current_node["NAME"])
print(current_node["POPULATION"])

