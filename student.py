# Some data cant just be represented by data type string or number
# Using class, we can define a bunch of attribute to define a variable
# we can define variables/attributes and functions/method in class


class Student:

    def __init__(self, name, major, gpa, is_on_probation):   #initialise function that will store all data into these parameter
        self.name = name     # passing the attributes to the object self
        self.major = major   # actual variable major is called major. Since we have not really define this before
        self.gpa = gpa       # self needed for multiples objects for a class
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False


