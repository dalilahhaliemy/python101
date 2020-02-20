'''
There are 6 data types in python:

1. None
- not assign to any value
- similar to null

2. Numeric
a) int - whole number
b) float - with decimals
c) complex - with imaginary number
d) bool/boolean - true(1) or false(0)

3. List
- defining the data by using []
- mutable

4. Tuple
- defining the data by using ()
- immutable
- but can add another tuple on top of the tuple

5. Set
- defining the data by using {}
- mutable
- omitting the sequence and the duplicates

6. String
- name or anything, can be in written number '21'
- user input by default has thi data type

7. Range

8. Dictionary
- use {} since we don't want key to be repeated
- we also done care about the sequence, so we gonna use set to define this

'''


# to check data type of a variable use type()

x = 3.089
print(type(x))                  # it will show float
print(complex(3, 5))            # to create a complex value
bool_true = True
bool_false = False
print(int(bool_true))           # true represent 1
print(int(bool_false))          # false represent 0
print(bool_true.__bool__())     # print the value that has 2 outcome T/F
print(bool_false.__bool__())    # print the value that has 2 outcome T/F


# list

lst = [22, 23, 25, 64, 22]
print(type(lst))                # it will show list
print(lst)


# set

st = {22, 23, 25, 64, 22}
print(type(st))                # it will show set
print(st)                      # omit duplicates
st.add(24)
print(st)


# tuple

tpl = (22, 23, 25, 64, 22)
tp2 = (1, 2, 3, 5)
print(type(tpl))                # it will show list
print(tpl)
print(tpl.__add__(tp2))         # adding a tuple on top of the previous tuple


# range

print(range(5))
print(list(range(5)))           # to see all range and put it in list
range(4, 12, 2)                 # start 4, stop 12 (exclusive), diff 2
print(list(range(4, 12, 2)))


# dictionaries

dtn = {"Navin": "Samsung", "Rahul": "iPhone", "Kiran": "OnePlus"}
print(dtn)
print(dtn.keys())              # to print all keys in dtn dictionaries
print(dtn.values())            # to print all values in dtn dictionaries

print(dtn["Rahul"])            # getting values using [key]
print(dtn.get("Kiran"))        # getting values using .get

for k, v in dtn.items():       # to print all items in dictionaries
    print(k + " using " + v)

