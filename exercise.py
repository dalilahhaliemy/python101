'''
print("You woke up")

hungry = input("Are you hungry?: ")
if hungry == "yes":
    print("Go eat breakfast")
else:
    print("Dont go eat breakfast")

print("\nYou left the house")

cloudy = input("Is it cloudy?: ")
if cloudy == "yes":
    print("Please bring an umbrella")
else:
    print("Please bring a sunglasses")

print("\nYou at the restaurant")

eat = input("What do you wanna eat?: ")
if eat == "meat":
    print("Please order a steak")
elif eat == "pasta":
    print("Please order spaghetti & meatballs")
else:
    print("Please order a salad")

###########################################################################

import modules     # To check the file or module origin, ctrl+b
print(modules.roll_dice(10))
print(modules.feet_in_mile)

# exercise combine list by index
ages = [56, 83, 40, 39]
a = modules.beatles[0] + " is " + str(ages[0]) + " years old."
b = modules.beatles[1] + " is " + str(ages[1]) + " years old."
c = modules.beatles[2] + " is " + str(ages[2]) + " years old."
d = modules.beatles[3] + " is " + str(ages[3]) + " years old."

name_age = [a, b, c, d]
print(name_age)


# exercise combine list by index using while loop
ages = [56, 83, 40, 39]
i = 0
new = [" ", " ", " ", " "]
while i <= 3:
    new[i] = modules.beatles[i] + " is " + str(ages[i]) + " years old."
    i = i + 1
print(new)


# OR we can use Zip for this
ages = [56, 83, 40, 39]
b = ["is", "is", "is", "is"]
d = ["years old", "years old", "years old", "years old"]

name_age_2 = zip(modules.beatles, b, ages, d)

for a, b, c, d in name_age_2:
    print(a, b, c, d)

'''
###########################################################################


def fact(x):                  # say we wanna build a factorial function
    result = 1
    for i in range(1, x+1):
        result *= i
    return result


print(fact(5))
print(5*4*3*2*1)
print(fact(3))
