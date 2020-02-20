'''
- Methods is functions defined in a Class
1. Instance method: function that works for the object. It has 2 type :
a) Accessor Method: accessing the object
b) Mutator Method: mutate/change the object
2. Class method: class variable can only use here)
3. Static method: functions that does not concern instance nor class variable
'''


class Student:

    school = "Telusko"             # Class variable can ONLY be used in Class method

    def __init__(self, m1, m2, m3):
        self.m1 = m1               # instance variables can ONLY be used in instance method
        self.m2 = m2
        self.m3 = m3

    def avg(self):                 # instance method : Works for the object
        return (self.m1 + self.m2 + self.m3)/3

    def get_m1(self):              # ACCESSOR METHOD
        return self.m1

    def change_m1(self, value):    # MUTATOR METHOD
        self.m1 = value

    @classmethod                   # need to define here first if we gonna add Class Method
    def get_school(cls):           # CLASS METHOD
        print(cls.school)          # need to define cls(class) here since it is class variable, not object(self)

    @staticmethod                  # STATIC METHOD. need to define here
    def info():                    # blank () since it is neither related to object nor class variable
        print("This is a Student class")


s1 = Student(11, 12, 13)           # assigning object to the class
s2 = Student(30, 40, 50)

print(s1.avg())                    # use instance method by specifying the object (since object is instance variable)
print(s2.get_m1())
s2.change_m1(31)
print(s2.get_m1())

Student.get_school()                     # get the class variable using class method
Student.info()
