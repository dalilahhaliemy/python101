# Using DECORATOR to add some new logic to an existing function
# say we have a division function
def div(a, b):
    print(a/b)


div(4, 2)
div(2, 4)


# say we want to add a new logic to the function where denominator is the smaller value (b must be < a)
# we can use decorator without changing div function
def new_logic(func):    # we will need to input function here inside this new logic

    def inner(a, b):       # this function should has same arguments as the div function (the function we wanna modify)
        if b > a:          # now write the new logic you want to change
            a, b = b, a            # swapping a and b to ensure a must be greater than b
        return func(a, b)  # after swapping, we call the function again (original function)
    return inner           # return inner function result to new_logic function. Now the new_logic function has the added logic


new_div = new_logic(div)
new_div(2, 4)


# exercise using decorator
# say we want to change the function in such a way we only divide the number, if there is no remainder
def new_logic_2(func):

    def inner(a, b):
        if a % b != 0:
            print("Not able to do division")
        else:
            return func(a, b)
    return inner


new_div_2 = new_logic_2(div)

div(9, 3)
new_div_2(5, 2)
new_div_2(10, 5)
