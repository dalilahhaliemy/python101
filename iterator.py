# normal way to iterate is using for loop
nums = [7, 8, 9, 5]

#for i in nums:
#    print(i)


# Using ITER() function for iteration
it = iter(nums)
print(it)        # This will give error since we cant print iterable object variable
print(it.__next__())    # next is a built in function for iter(). It calls the first object
print(it.__next__())    # it will remember the previous iteration in it variable
print(it.__next__())
print(next(it))         # can also use something like this. beyond this will throw error, since it only has 4 iteration


# note that this way, it does not remember the previous iteration. Thus we need to use a variable like above
print(iter(nums).__next__())
print(iter(nums).__next__())


# say we wanna print Top Ten numbers, we can use our own iteration method
# to print an object, lets use a Class function
# first, we need to set a starting point, number 1
class TopTen:

    def __init__(self):
        self.num = 1

    def __iter__(self):   # we need this to make the objects iterable. Else it wont be iterable and we can't use looping
        return self

    def __next__(self):   # this will give the next value
        if self.num <= 10:      # stopping at 10
            value = self.num    # printing this now, not +1
            self.num += 1       # for next iteration
            return value
        else:
            raise StopIteration


values = TopTen()         # Class TopTen has 10 objects that are iterable. Those values are in 'values' variable
print(next(values))       # =1
print(next(values))       # =2
for i in values:          # this will continue from 3 onwards. That is iteration. It will rmb the previous printed iteration
    print(i)


# Using GENERATOR for ITERATOR
# generator is a function that will behave as iterator
# this way, we don't need to use a Class object for iterator
def topten():

    yield 1    # instead of using return, we are using yield. This will give output in iterable object format
    yield 2
    yield 3
    yield 4


val = topten()
'''print(val)'''     # this does not work cause it is a generator, same as we cant print iterable variable object
print(next(val))     # use iteration method for this
print(next(val))
for i in val:
    print(i)         # it will rmb the previous printed iteration, since it is iterator


# another example, say we want to get top 10 perfect square
def ten_perfect_square():

    n = 1

    while n <= 10:
        sq = n*n
        yield sq           # this will return iterable object
        n += 1


val2 = ten_perfect_square()
for i in val2:
    print(i)
