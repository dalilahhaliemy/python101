# Arguments are when we have more than 1 variables
# setting a default value if no option is taken
def get_gender(sex="Unknown"):    # setting the default value

    if sex is "m":
        sex = "Male"
    elif sex is "f":
        sex = "Female"
    print(sex)


get_gender("m")
get_gender("f")
get_gender()


# KEY ARGUMENTS
def random_sentence(name="Bucky", action="ate", item="tuna"):
    print(name, action, item)


random_sentence()                             # this will take the default value
random_sentence("Sally", "sleep", "gently")
random_sentence(item="shoes")              # the rest will take default value
random_sentence(item="awesome", action="is")  # this is keyword arguments. we can send in any order


# using * to define unknown number of key arguments
# sometimes we dunno how many variable/arguments in the function that we wanna define
# using *args means we will not have to define the variables/key arguments in the 1st line of the function
def add_numbers(*args):             # just use this instead
    total = 0
    for a in args:
        total += a                   # total = total + a
    print(total)


add_numbers(3)                       # total this number (1 variable)
add_numbers(3, 32)                   # total these numbers (2 variable / 2 arguments)
add_numbers(3, 34343, 3434, 454)     # 4 arguments

'''
# another example
def sum_all(a, *b):
    c = a + b
    print(c)


sum_all(3, 5, 10, 20)     # this will give error since all other variable, 5-20 is in tuple b. we cant add integer with tuple
'''


def sum_all_2(a, *b):     # thus need to modify the function
    c = a
    for i in b:
        c += i            # increment a by all i in b
    print(c)


sum_all_2(3, 5, 10, 20)


# Unpacking arguments
def health_calculator(age, apples_ate, cigs_smoked):
    answer = (100-age) + (apples_ate*3.5) - (cigs_smoked*2)
    print(answer)


buckys_data = [27, 20, 0]    # age, apples ate, cigs smoked

health_calculator(buckys_data[0], buckys_data[1], buckys_data[2])
health_calculator(*buckys_data)    # unpacked the list, so will pass as 3 numbers without having to extract one by one by indexing


# Passing by value VS Passing by variable/reference
def update(x):
    x = 8
    print("x", x)


a = 10
update(a)            # this is Pass by value
print("a", a)        # this will still show 10 since we are not passing variable a to be updated, we are passing the value a to be updated


# setting variable for arguments
def person(name, *data):
    print(name)
    print(data)                          # this will be a tuple, thus it is better for us to assign variable to it


person("Navin", 28, "Mumbai", 9788789)


# to assign keyword/variable, we need to set **data
def person(name, **data):
    print(name)
    for i, j in data.items():      # i, j = key, data
        print(i, j)


person("Navin", age=28, city="Mumbai", mob=9788789)  # assigning keyword/variable.
