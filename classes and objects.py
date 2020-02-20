'''
from student import Student     # from student file, import Student class

student1 = Student("Jim", "Business", 3.5, False)    # This is one object in a class (student)
student2 = Student("Pam", "Art", 2.5, True)          # assigning an object to a Class

print(student1.name)      # cant print(Student) since it is a class, not a variable
print(student1.major)     # cant print(student1) since it is not a data string type or variable. it is an object
print(student1.gpa)
print(student1.is_on_probation)


print(student1.on_honor_roll())
print(student2.on_honor_roll())


# Class variables and instance variables
class Girl:

    gender = "Female"       # this is a class variable. For every object they will have the same class variable

    def __init__(self, name, age):  # this is constructor
        self.name = name    # this is an instance variable. For each object, they will have unique instance variable that defines their attributes
        self.age = age      # this is an instance variable too


girl1 = Girl("Rachel", "23")      # assigning an object
girl2 = Girl("Monica", "25")      # assigning an object
print(girl1.name)
print(girl2.age)
print(girl1.gender)
print(girl2.gender)
print(girl1)                      # this is useful to define a shared variable in class

Girl.gender = "Male"              # Changing Class Variable
print(girl1.name, girl1.gender)
print(girl2.name, girl2.gender)


# Understanding SELF
# say we have a class Computer in which we have multiple functions in it
class User:

    def __init__(self):            # for all objects, will have this attributes
        self.name = "Navin"
        self.age = 28

    def update_age(self):          # defining a function that will update the age to be 30
        self.age = 30

    def compare_age(self, y):
        if self.age == y.age:                    # u1.age == u2.age
            print("They are of the same age")
        else:
            print("They are not the same age")


u1 = User()    # assigning object to a class
u2 = User()

print(u1.name, u1.age)            # since we are not running the update function, both age will be 28
print(u2.name, u2.age)

u2.name = "Rahul"                 # changing the value

u1.update_age()                   # this is where SELF is important. SELF.update_age (means, c1.update_age)
print(u1.name, u1.age)
print(u2.name, u2.age)

u1.compare_age(u2)                # u1 is SELF here, y is u2


# another example
class Enemy:
    life = 3

    def attack(self):            # use something in the class
        print("ouch!")
        self.life -= 1           # use the variable in the Enemy class

    def check_life(self):
        if self.life <= 0:
            print("I am dead")
        else:
            print(str(self.life) + " life left")    # print amount of life that they have left


enemy1 = Enemy()      # defining object enemy1 is from Enemy class
                      # need to create an object assigned to the class, then we can use the function
enemy1.attack()
enemy1.attack()
enemy1.check_life()

enemy2 = Enemy()       # another object
enemy2.check_life()


# another example
class Tuna:

    def __init__(self):
        print("blbrblrb")

    def swim(self):
        print("I am swimming")


flipper = Tuna()              # assigning object to the Tuna class
flipper.swim()                # it will call innit function first regardless. This is the function of innit


# say we are building a video game which all have enemy character
class Enemy2:

    def __init__(self, energy):    # inputting variable in the init function/constructor
        self.energy = energy

    def get_energy(self):
        print(self.energy)


# assigning object to a Enemy2 class
jason = Enemy2(5)
sandy = Enemy2(18)

# to use the function, we need to specify the object that we want to call the function
# cause behaviour(function) is depends on the object
jason.get_energy()       # calling the get_energy function to jason object. (get energy for jason). Else to whom we should give energy?
sandy.get_energy()

# or

Enemy2.get_energy(jason)
Enemy2.get_energy(sandy)
'''

# Variable inside a class funtions


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greetings(self):
        print(f"Hi, {self.name}! You are {self.age} years old")


data1 = Person("John", "34")
data1.greetings()