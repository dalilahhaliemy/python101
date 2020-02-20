character_name = "John"
character_age = "35"

print("There was a man named " + character_name +".")
print("He was " + character_age + " years old.")
print("He really liked the name " + character_name + ",")
print("but didn't like being " + character_age + ".")
print("Test1", "Test2")
# swapping variable
a = 5
b = 6

a = b
b = a               # this is not swapping as we lost 5
print(a)
print(b)


a = 5
b = 6
temp = a            # store value 5 here, temp variable
a = b               # a = 6 here
b = temp               # b = 5 here
print(a)
print(b)


# swapping without using a third variable
a = 5
b = 6
a, b = b, a           # they rotate the value
print(a)
print(b)


# GLOBAL vs LOCAL variable
a = 10      # global variable

# local variable can only be access in the variable
# local function does not affect the global variable outside the function
def something():
    a = 15      # local function. If we do want to change the value here, need to mention it is a global variable
    b = 8
    print("in function", a)


something()

print("outside", a)     # local variable does not affect global variable

# if we dont define a in the function, it still can work since a is global variable


def something2():
    global a          # this will afffect outside a as well. Re-assign the variable
    a = 15
    b = 8
    print("in function", a)


something2()

print("outside", a)     # since variable in the function is global variable, it re-assign the variable


# say we wanna change the global variable in the function, while keeping our local variable value
a = 10


def something3():
    a = 5
    globals()["a"] = 15
    print("inside function", a)


something3()

print("outside", a)     # using globals to keep local variable value while changing the global variable in the function
