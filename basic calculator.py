print(3+4.5)
print(10 % 3)

my_num = -5
print(my_num)

print(str(my_num) + " is my favourite number")
print(abs(my_num))
print(pow(3, 2))
print(max(3, 2))
print(round(3.7))

from math import*
print(floor(3.7))       # floor means round down
print(ceil(3.7))        # ceil means round up
print(sqrt(36))
print()

# assignment operator (assigning a variable to another
# using += or -= or *= or /=
x = 2
x += 2     # increment x by 2 (newx = x + 2)
print(x)   # this will say 4

y = 3
y *= 2     # multiplying y with 2 (newy = y * 3)
print(y)   # this will say 6

z = 8
z /= 2
print(z)


# assigning variables
a, b = 5, 6
print(a)


# unary operator
n = 7
print(-n)

# rational operator
print(a < b)    # a, b = 5, 6
print(a > b)
print(a == b)
print(a <= b)
print(a != b)

# logical operator (or, and, not)
a, b = 5, 4
print(a < 8 and b < 5)
print(a < 8 and b < 2)

m = True
print(m)
print(not m)
