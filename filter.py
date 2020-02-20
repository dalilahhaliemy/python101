# Using FILTER to filter out a list
# say we want to filter a list and take out only even number
# filter take a list, and filter the list based on a function
# it takes the argument filter(function, list)

# first, define a list that we want to filter
nums = [3, 2, 6, 8, 4, 6, 2, 9]


# next, define the function that we want to filter out
def is_even(n):
    return n % 2 == 0            # give boolean value. True or False


# assign a set of list to the filter function. Use list() here to put the sequence in a list
evens = list(filter(is_even, nums))
print(evens)


# using lambda for this since definition of function here is not efficient
odds = list(filter(lambda n: n % 2 != 0, nums))       # this
print(odds)


# Using MAP to modify the values of all the data in the list
# say we want to double all values in the list, we can use map()
# it takes the argument map(function, list)
doubles = list(map(lambda n: n*2, evens))
print(doubles)


# Using REDUCE to
# it takes the argument reduce(function, list)
# say we want to add all these values
from functools import reduce

sum_all = reduce(lambda a, b: a+b, doubles)
print(sum_all)
