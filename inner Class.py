# Class within a Class
# say we have a Class student
class Student:

    def __init__(self, name, roll_num):
        self.name = name
        self.roll_num = roll_num

    def show(self):
        print(self.name, self.roll_num)


s1 = Student("Harry", 4)
s2 = Student("Hermione", 5)

s1.show()
s2.show()


# say each student have laptop
# These laptop has their own attributes. Thus, we need a class for them
class Student2:

    def __init__(self, name, roll_num, brand, ram):   # this defines all the variable for the objects of the class
        self.name = name
        self.roll_num = roll_num
        self.laptop = self.Laptop(brand, ram)     # 1. assign inner class object inside the outer class here OR

    def show(self):
        print(self.name, self.roll_num)

    class Laptop:

        def __init__(self, brand, ram):
            self.brand = brand
            self.ram = ram

        def show(self):
            print(self.brand, self.ram)

    class House:                          # 2. do not assign the inner class object here. we assign outside outer class

        def __init__(self):
            self.house_name = "Gryffindor"
            self.score = 100


s1 = Student2("Harry", 4, "MacBook", 128)
s2 = Student2("Hermione", 5, "HP", 64)

s1.show()
s1.laptop.show()          # get the method of the inner class
print(s1.laptop.ram)      # get the instance variable of the inner class
print(s2.laptop.brand)


# OR 2. assigning the inner class object outside outer class
house1 = Student2.House()
house2 = Student2.House()

print(house1.house_name, house1.score)
