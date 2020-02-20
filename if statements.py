# to execute a set of code if it met certain criteria
'''
I wake up
If i'm hungry      ----> condition. If true, go to following line
   I eat breakfast  ---> if false, skip this and just go through following line

I leave my house
If its cloudy
   I bring umbrella
otherwise            ----> if false, follow line below
   I bring sunglasses

Im at restaurant
If I want meat
   I order a steak
otherwise if I want pasta
   I order spaghetti & meatballs
otherwise
   I order a salad
'''

is_male = False

if is_male:                  # if this is correct, then print below
    print("You are male.")
else:                        # if not, print below
    print("You are not a male")


# set 2 condition, say male and tall
is_male = False
is_tall = False

if is_male or is_tall:      # using OR in statements
    print("You are male or tall or both.")
else:
    print("You are neither male nor tall")


# using and in statements
is_male = True
is_tall = True

if is_male and is_tall:
    print("You are tall male")
else:
    print("You are not a tall male")


# using elif for negative condition
is_male = False
is_tall = True

if is_male and is_tall:
    print("You are tall male")
elif is_male and not(is_tall):       # check for another option
    print("You are a short male")
elif not(is_male) and not(is_tall):
    print("You are a short female")
else:                                # if we run all the option, but it doesnt satisfies all, thus, print below
    print("You are a tall female")


# say we wanna build a function that will print out the maximum values of a set of data

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1         # remember to use return since we need the function to return us a value in calculation
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(100,4,5))