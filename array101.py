# need to have values in same type, if one num, then all num
# say we need to create a variable for 100 students each have their own mark, we can use array for this

# import array as arr   # this way subsequent is just arr.xxxx instead of array.xxx
from array import *

vals = array('i', [5, 9, 8, 4, 2])   # array of signed integer(-ve and +ve) [this is the code. lookup for more]
print(vals)