'''
# to be used over and over again, we can put a set of code in the function then we can just call it whenever we want
def say_hi():
    print("Hello user")   # it wont print here cause we did'nt notify python that we wanna use this function


print("Top")
say_hi()                  # here we asking it to call the function
print("Bottom")


# setting a variable in the function, say name
def say_hi(name):
    print("Hello " + name)


say_hi("Mike")


# set 2 variables in the function, say name and age
def say_hi(name, age):
    print("Hello " + name + ", you are " + age)


say_hi("Mike", "35")
say_hi("Steve", "27")


# if user input number format, we need to convert them first before printing a string out
def say_hi(name, age):
    print("Hello " + name + ", you are " + str(age))


say_hi("Mike", 35)


# RETURN STATEMENTS
# for function that involve calculation, we need to store the result in a variable, thus we need to use return statement
def cube(num):
    num*num*num


print(cube(3))    # this will show None. We need a return statement since we dont define the result of this calculation


def cube(num):
    return num*num*num     # defining result using return function. Storing the value of the result to a function. =


print(cube(3))

result = cube(4)    # set a variable as the result to make codes prettier and store the value
print(result)
'''


# another example
def hello_function():
    print("Hello function!")

hello_function()                    # no need to use print since the function is a print function


def hello_function2():
    return "Hello function"        # this means the function = the value of string "Hello function!"

hello_function2()                  # calling this wont show anything, it just stating that the function has value


'''
# return 2 values
def add_sub(x, y):
    c = x + y
    d = x - y
    return c, d


result1, result2 = add_sub(10, 2)

print(result1, result2)


def bitcoin_to_usd(btc):
    amount = btc * 527
    print(amount)


bitcoin_to_usd(3.85)      # how many usd for 3.85 btc


# Using LIST in a function
# say we wanna create 2 function that will give us odd and even number
number_set = [32, 33, 33, 57, 78, 90, 83]


def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return odd, even


a, b = count(number_set)
print("Odd:", a)
print("Even:", b)

# or

print("Even : {} and Odd : {}".format(b, a))


# RECURSION, a function calling itself

import sys

print(sys.getrecursionlimit())

i = 0


def greet():
    global i       # to allow we use i in this function
    i += 1
    print("Hello", i)
    greet()


greet()



# using recursion in factorial function
def fact(x):
    if x == 0:
        return 1
    return x * fact(x-1)


print(fact(5))    # 5! = 5*4! = 5*4*3! etc...


# using LAMBDA for nameless function
def square(a):
    return a*a     # too many unnecessary lines. we only need this line actually


result3 = square(5)
print(result3)


f_func = lambda a: a*a
result3 = f_func(5)
print(result3)


# Using 2 variable in the lambda
g_func = lambda a, b: a*b
result4 = g_func(3, 4)
print(result4)
'''