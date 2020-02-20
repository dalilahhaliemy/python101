class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a, b):
        s = a + b
        return s


s1 = Student(33, 44)
print(s1.sum(3, 4))
'''print(s1.sum(3, 4, 2))'''      # this will give error since we only define 2 variable


# say we wanna input > 2 variables
class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None):    # setting default value to None if there is no input
        s = a + b + c
        return s


s1 = Student(33, 44)
'''print(s1.sum(3, 1))'''
# this does not work since c=None, adding integer and None does not work
# hence we need to add more validation into the function -> METHOD OVERLOADING


class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None):    # setting default value to None if there is no input

        if a!=None and b!=None and c!=None:
            s = a + b + c
        elif a!=None and b!=None:
            s = a + b
        else:
            s = a

        return s


s1 = Student(33, 44)
print(s1.sum(3, 1, 4))
print(s1.sum(3, 4))
print(s1.sum(3))


# METHOD OVERRIDING
class A:

    def show(self):
        print("in A show")


class B(A):
    pass


a1 = A()
a1.show()
b1 = B()
b1.show()            # since B does not have show, it will use method in A


class B(A):

    def show(self):
        print("in B show")


b1 = B()
b1.show()           # now it will take the method show in Class B -> METHOD OVERRIDING

