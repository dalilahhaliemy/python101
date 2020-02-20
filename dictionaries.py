# using dictionaries to store a key values that we will be using frequently.
# use {} for creating a set
# note that all key must be unique

monthConversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversion["Feb"])


# can also use get function
print(monthConversion.get("Nov"))
print(monthConversion.get("Luv", "Not a valid key"))  # if error, print the following


# dictionaries can also be in a set of number
dayConversion = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
}

print(dayConversion[1])
print(dayConversion.get(3))


# sorting dictionaries using zip

stocks = {
    'GOOG': 520.54,
    'FB': 76.45,
    'YHOO': 39.28,
    'AMZN': 306.21,
    'AAPL': 99.76
}

merged = zip(stocks.values(), stocks.keys())   # merged now is a tuple

for a, b in merged:
    print(a, b)

print(min(zip(stocks.values(), stocks.keys())))     # cant use the tuple here
print(max(zip(stocks.values(), stocks.keys())))     # cant use the tuple here
print(sorted(zip(stocks.values(), stocks.keys())))  # if we sort by name, then use key first when zipping it


# finding smallest and largest item in a list & dictionaries
import heapq

grades = [32, 43, 654, 34, 132, 66, 99, 532]
print(heapq.nlargest(3, grades))   # finding top 3 grade

stocks = [                              # say we wanna find the largest items in a dictionary
    {'ticker': 'AAPL', 'price': 201},
    {'ticker': 'GOOG', 'price': 800},
    {'ticker': 'F', 'price': 54},
    {'ticker': 'MSFT', 'price': 313},
    {'ticker': 'TUNA', 'price': 68}
]

# since it is not just 1 value, need to add attribute (3rd argument)
print(heapq.nsmallest(2, stocks, key=lambda stock: stock['price']))


# another example
student = {
    "name": "John",
    "age": 25,
    "course": ["Math", "CompSci"]
}


print(student)
print(student["name"])
print(student.get("name"))
print(student.get("phone", "Key does not exist"))    # try to access a non-existing key


# to know available keys in a dictionaries
print(student.keys())
print(student.values())
print(student.items())           # show each items (key and values pair)


# adding new key to the dictionaries
student["phone"] = "555-5555"
print(student.get("phone"))


# update values of a key
student["name"] = "Jane"
print(student)


# update multiples values of keys at once
student.update({
    "name": "Jenny",
    "age": 70,
    "phone": "667-6778"
})

print(student)


# delete a key in a dictionaries
del student["age"]
print(student)

phone = student.pop("phone")     # or
print(student)
print("phone")


# using for loop with dictionaries
student = {
    "name": "John",
    "age": 25,
    "course": ["Math", "CompSci"]
}


for key in student:    # printing key only
    print(key)


for key, value in student.items():   # since items will give a pair (key, value)
    print(key, value)


# another example
