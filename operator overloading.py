# Class is an empty function
# built in functions like add, subtract, printing object as a list, is not defined in the Class
# to use these function for class objects, we need to define them in the Class


# Defining ADD __add__ in Class
class Numbers:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2


num1 = Numbers(20, 30)
num2 = Numbers(1, 3)

'''result1 = num1 + num2'''         # this will show error since + is not defined in class Numbers


# we need to define the __add__ operator in the class
class Numbers:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        a1 = self.m1 + other.m1
        a2 = self.m2 + other.m2
        result = Numbers(a1, a2)    # creating object of Number Class for the result
        return result               # returning the result object


num1 = Numbers(20, 50)
num2 = Numbers(1, 3)

result1 = num1 + num2          # Numbers.__add__(num1, num2). NOTE THAT result1 is an object, as defined in the function
print(result1.m1, result1.m2)  # since result1 is a class object, we need to specify which attributed we want to print

'''
if num1 > num2:                 # This will show error since class don't have > function
    print("Num1 wins!")         # we need to define this in the Class
else:
    print("Num2 wins!")
'''

# Defining > __gt__ in Class (greater than)
class Numbers:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        a1 = self.m1 + other.m1
        a2 = self.m2 + other.m2
        result = Numbers(a1, a2)    # creating object of Number Class for the result
        return result

    def __gt__(self, other):
        b1 = self.m1 + self.m2
        b2 = other.m1 + other.m2

        if b1 > b2:            # defining the > operator
            return True        # we need to compare the value immediately, hence, no need to store the result in an object
        else:
            return False


num1 = Numbers(20, 30)
num2 = Numbers(21, 30)
if num1 > num2:
    print("Num1 wins")
else:
    print("Num2 wins")


'''print(num1)'''              # this does not work since we don't define printing object string in the class
# Defining PRINT OBJECT __str__ in Class
class Numbers:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        a1 = self.m1 + other.m1
        a2 = self.m2 + other.m2
        result = Numbers(a1, a2)    # creating object of Number Class for the result
        return result

    def __str__(self):
        return "{} {}".format(self.m1, self.m2)    # convert them into a string


num1 = Numbers(20, 50)
num2 = Numbers(1, 3)

result1 = num1 + num2
print(num1)
print(result1)                # we can print objects, now

