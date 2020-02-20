# a FOR LOOP will “do” something to everything which you wish to iterate through.
# for sequence
# in other words, for all the element, run the codes in loop
'''
for letter in "Giraffe Academy":  # set a variable here in the string. For each variable (name as letter) in the string
    print(letter)      # for all the element of the defined variable, loop this function

for index in range(10):   # note that it will exclude 10 since it start with 0
    print(index)

for index in range(3, 10): # will print 3-9 (exclude 10)
    print(index)

friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
    print(friend)

print(len(friends))

# to print all the elements in the array using index
for index in range(len(friends)):
    print(friends[index])      # friends[0] friends[1] friends[2]

# using if statements in for loop
for index in range(5):
    if index == 0:
        print("First iteration")
    else:
        print("Not first iteration")

print("\n")


for i in range(1, 21):
    if i % 5 != 0:           # Dont want to print numbers divisible by 5
        print(i)


# using loops for multiplication
def raise_to_power(base_num, pow_num):    #set 2 variables in the function
    result = 1                            #set an empty variable to store the result later
    for index in range(pow_num):          #will loop through all index in pow_num
        result = result*base_num
        print(result)                     #will show the result for each iteration (times base number)
    return result                         #will only return the last iteration since that was the latest result value


print(raise_to_power(3, 4))


# BREAKING a loop halfway
# say we wanna loop through a range to find a specific number, once we got it, we want to stop the loop

magic_number = 26

for num in range(101):          # search the magic number from 0-100
    if num is magic_number:
        print(str(num) + " is the magic number")
        break                   # break the loop once we have satisfy this condition
    else:
        print(num)


# another example, say we wanna give candy to the user but we only have limited amount of candy
available = 3     # say we only have maximum amount of candy
x = int(input("How many candies that you want? "))
i = 1
while i <= x:      # check for available candy first before printing candy
    if i <= available:
        print("Candy")
        i += 1
    else:
        print("We can only give u 3 candies")
        break      # break the loop once we have satisfy this condition


# another example, say we want to print numbers that are not divisible by 5 nor 3
for i in range(1, 101):
    if i % 3 != 0:
        if i % 5 != 0:
            print(i)

# another way to do this is by using CONTINUE in a loop
for i in range(1, 101):
    if i % 3 == 0 or i % 5 == 0:       # if the number divisible by 3, skip this (or 'continue' the loop)
        continue
    print(i)
'''

# CONTINUE in a loop
# say we wanna know what number left in a range of 1-20 excluding the number taken

numbers_taken = [2, 5, 12, 13, 17]

for number in range(1, 21):
    if number in numbers_taken:
        continue                    # immediately go to the next iteration, anything below this code wont get executed
    print(number)                   # print if it is not in numbers taken


# another example, say we don't want to print #3
for i in range(1, 6):

    if i == 3:
        continue             # immediately go to the next iteration if i=3, anything below this wont get executed

    print("Hello", i)



for i in range(1, 6):

    if i == 3:               # if this condition satisfied, loop stop here. break out from the loop
        break

    print("Hello", i)



# PASS in a loop
# say we dont want to print odd numbers
for i in range(1, 101):
    if i % 2 != 0:
        pass            # but we dont have an instruction, thus use pass.
    else:
        print(i)


# another example
def fun():
    pass       # need to define something here, else will show error.  we can use pass if we dont have any instruction or definition

fun()

'''
# another example
# say we wanna print
# (0,1)
# (0,2)
# (0,3)
# (0,4)

for x in range(1):
    for y in range(1, 5):
        print(f"({x},{y})")