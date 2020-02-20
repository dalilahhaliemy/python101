from Chef import Chef
from ChineseChef import ChineseChef

myChef = Chef()

myChef.make_chicken()              # we can use this if there is a function in it
myChef.make_salad()
myChef.make_special_dish()

myChineseChef = ChineseChef()

myChineseChef.make_chicken()
myChineseChef.make_salad()
myChineseChef.make_special_dish()
myChineseChef.make_fried_rice()


# another example of inheritance
class Parent:

    def print_last_name(self):
        print("Roberts")


class Child(Parent):

    def print_first_name(self):
        print("Bucky")


# print_last_name()        # this will show error since we have not assign an object to a class
# print_first_name()       # NEED TO ASSIGN AN OBJECT FIRST

bucky = Child()            # assign an object to a child class
bucky.print_first_name()   # object.function
bucky.print_last_name()    # inherit from Parent class


# MULTIPLE INHERITANCE
class Mario:

    def move(self):
        print("I am moving!")


class Shroom:

    def eat_shroom(self):
        print("Now I am big!")


# say we wanna have a class who inherit both of these class
class BigMario(Mario, Shroom):
    pass           # if we don't have any definition, we can use this, else, empty line will show error


bm = BigMario()    # assigning an object to a class
bm.move()          # this object inherits functions from the previous 2 class
bm.eat_shroom()


# Constructor in inheritance (__init__)
class A:

    def __init__(self):
        print("in A __init__")

    def feature1(self):
        print("feature 1 is working")

    def feature2(self):
        print("feature 2 is working")


class B(A):

    def feature3(self):
        print("feature 3 is working")

    def feature4(self):
        print("feature 4 is working")


a1 = A()
b1 = B()          # class object B inherit constructor class A as well IF B don't have constructor


# if both class have init (constructor)
class C:

    def __init__(self):
        print("in C __init__")

    def feature1(self):
        print("feature 1 is working")

    def feature2(self):
        print("feature 2 is working")


class D(C):

    def __init__(self):
        super().__init__()           # want to access super class constructor as well (class C)
        print("in D __init__")

    def feature3(self):
        print("feature 3 is working")

    def feature4(self):
        print("feature 4 is working")

    def feat(self):
        super().feature1()


c1 = C()
d1 = D()               # this will take its own constructor since it is defined
d1.feat()

