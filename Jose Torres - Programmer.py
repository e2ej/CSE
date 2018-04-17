class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print("%s is going to work." % self.name)


class Employee(Person):
    def __init__(self, name, age, job, wage):
        super(Employee, self).__init__(name, age)
        self.job = job
        self.wage = wage


class Programmer(Employee):
    def __init__(self, name, age, job, wage, computer, code):
        super(Programmer, self).__init__(name, age, job, wage,)
        self.computer = computer
        self.code = code

    def code(self):
        print('The programmer coded a game.')
