# say we only want the numbers divisible by 5
nums = [12, 16, 18, 20, 25]

for num in nums:
    if num % 5 == 0:
        print(num)    # this will list all numbers that divisible by 5


# say we want to print only one number that divisible by 5, we can use break
for num in nums:
    if num % 5 == 0:
        print(num)
        break         # this will break the loop once it hit once the condition


# say we do not have any numbers divisible by 5
nums = [12, 16, 18, 21, 26]

for num in nums:
    if num % 5 == 0:
        print(num)
    else:
        print("not found")   # this will print 5 times for all the num in nums. Since this 'else' is for 'if'


# we can avoid such cases by using FOR ELSE.
nums = [11, 16, 18, 21, 26]

for num in nums:
    if num % 5 == 0:
        print(num)
        break             # need to add break here, else, it will still print not found since it does not get out of the loop still if this condition is met. (only print one number divisible by 5)
else:
    print("not found")    # this will only print once since the else is for 'for'. it is outside if loop


# another example, say we want to find prime number (divisible by 1 and only by itself)
# first we check if this number divisible by 2 and so on, until n-1. eg: 4/2?, 4/3? if any of this %=0, then it is divisible
number = 4

for i in range(2, number):
    if number % i == 0:
        print(number, "is not prime number")
        print("This number divisible by", i)
        break
else:
    print(number, "is a prime number")
