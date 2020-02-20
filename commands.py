'''
print("Giraffe\nAcademy")   # \n means new line
print(r"c:\docs\navin")     # printing raw string (means don't try to convert the string

print("Giraffe \"Academy")
print("Giraffe\Academy")
print('"Giraffe Academy"')
print("Giraffe's Academy")
print(5*"Giraffe ")

phrase = "Giraffe Academy"
print(phrase + " is cool")

print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))

print(phrase[14])
print(phrase.index("G"))
print(phrase.index("Acad"))

print(phrase.replace("Giraffe", "Elephant"))

print(phrase.isupper())

'''
# Printing Variable to a string
first = "John"
last = "Smith"
msg1 = first + " (" + last + ") " + "is a coder"
print(msg1)
# or
msg2 = f"{first} ({last}) is a coder"
print(msg2)


# FORMATTING A VARIABLE TO A STRING
num = input("Enter a number: ")
print("{} is a number".format(num))  # replace the num with the ones in the {}


def hello(greeting, weather="morning"):
    return "{}, {} you!".format(greeting, weather)


print(hello("Good", "afternoon"))
print(hello("Sad"))

'''
# printing pattern
print("# # # #")

print()

for i in range(4):             # can also use this way
    print("# ", end="")


print()
print()


for j in range(4):
    for i in range(4):  # can also use this way
        print("# ", end="")
    print()                   # run in the new line


print()


for j in range(4):
    for i in range(j + 1):  # can also use this way
        print("# ", end="")
    print()                   # run in the new line


print()


for j in range(4):
    for i in range(4 - j):  # can also use this way
        print("# ", end="")
    print()                   # run in the new line


# SPECIAL VARIABLE : __name__ and __main__
# __main__ means it is the current file that we are running
# __name__ is to know the current module that we are running

print("Commands: " + __name__)             # it will print __main__ here


def commands():
    print("Commands function excuted")     # if we import this file as module, it will print these 2 statements


commands()


# we can use the __name__ variable validation for this
# this way, when we import a module, the function would not be run together
if __name__ == "__main__":
    print("Commands 2: " + __name__)
    commands()
'''