import random       # import the whole file to be use here

# To check the file or module origin, ctrl+b

feet_in_mile = 5280
meters_in_kilometer = 1000
beatles = ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Star"]


def get_file_ext(filename):
    return filename[filename.index(".") + 1:]


def roll_dice(num):
    return random.randint(1, num)     # this means we are taking filename.function (random file, randint function)


print(roll_dice(10))


# SPECIAL VARIABLE : __name__ and __main__
# __main__ means it is the current file that we are running
# __name__ is to know the current module that we are running
from commands import commands    # when we run this, all other function in module will be ran as well
print("Modules: " + __name__)    # if we run this file, it will show __main__ here
