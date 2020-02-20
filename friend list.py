# LIST
# using [] to make a list
'''
friends = ["Kevin", "Karen", "Jim"]       # assign a variable in it

print(friends)
print(friends[-3])        # printing using index
print(friends[1:])        # 1 until the end

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

print(friends[1:4])       # 1 until excluding 4th element

friends[1] = "newKaren"
print(friends)
print(friends[1])

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends.extend(lucky_numbers)  # we can do all sorts of thing in a list. Explore by typing . a the end of the variable
print(friends)

friends.append("Creed")
print(friends)

friends.insert(1, "Kelly")
print(friends)

friends.remove("newKaren")
print(friends)

friends.clear()
print(friends)

friends = ["Kevin", "Karen", "Jim"]
# friends.pop()                # pop the last element out
pop_val = friends.pop()
print(pop_val)               # the value that was popped
friends.pop(0)               # index value
print(friends)
print(friends.index("Karen"))

friends = ["Kevin", "Karen", "Jim", "Jim"]
print(friends.count("Jim"))
friends.sort()
print(friends)

friends2 = friends.copy()
print(friends2)


# find character in a string
name = "Diyanah Dalilah"
print(name.find("y"))
print(name.find("d"))     # -1 means it does not exist
print(name.replace("Dalilah", "Didi"))
print(name)
print("Dalilah" in name)


# TUPLE
# using () to create tupple
coordinates = (4, 5)
print(coordinates[0])
print(coordinates.count(4))    # the element
# coordinates[1] = 10     This is a tuple. It cant be changed. Remove # to run the code


# SET
# using {} to create a set
# has no order
# set using the concept hash meaning we want speed other than sequence. It will omit duplicated values

set = {22, 25, 14, 21, 5}
print(set)                # notice it will change the sequence. This is because set omit sequence
# print(set[0])          # notice this will show error. Since it omit sequence, index will be invalid 
set2 = {25, 14, 98, 63, 75, 98}
print(set2)               # notice it will only show 98 once. Set will omit duplicated. Hash concept
set2.add(1)
print(set2)
'''
# set does not have order. It will just print random order with no duplicates
cs_courses = {"History", "Math", "Physics", "CompSci", "Math"}
print(cs_courses)

# say we wanna see what courses these set has in common
art_courses = {"History", "Math", "Art", "Design"}
print(cs_courses.intersection(art_courses))          # this will show the common course in both set

# say we wanna see the course in CS course but not in art course
print(cs_courses.difference(art_courses))

# say we wanna know all courses comnbined
print(cs_courses.union(art_courses))

'''
# unpacking list into variable
date, name, price = ["December 23, 2015", "Bread Gloves", 8.51]
print(date)


# unpacking list into function
# say we wanna take an average of a list, with omitting the first and last value in the list

grades = [23, 56, 67, 86, 90]


def drop_first_last(grades):
    first, *middle, last = grades     # this means, it will store the first value on the first variable, last value in last variable
    avg = sum(middle)/len(middle)     # anything in between will be stored in middle variable no matter how many the value are
    print(avg)


drop_first_last([23, 56, 67, 86, 90])
drop_first_last([23, 67, 67, 67, 67, 80])


# ANOTHER EXAMPLE
courses = ["History", "Math", "Physics", "CompSci"]

# to print all the items in list
for item in courses:
    print(item)

# to find whether the item exist in a list
print("Art" in courses)

# to print the item with its index
for index, course in enumerate(courses):
    print(index, course)

# say we wanna print all the items in a sentence
courses_str = ", ".join(courses)
print(courses_str)

# say we wanna split the whole sentences again to proper list
new_list = courses_str.split(", ")
print(new_list)
'''