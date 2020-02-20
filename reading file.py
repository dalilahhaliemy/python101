# To check if file is readable. It is a boolean
employee_file = open("employees", "r+")

print(employee_file.readable())

employee_file.close()


# To print out all elements in the file using READ() function
employee_file = open("employees", "r")        # opening a file

print(employee_file.read())

employee_file.close()


# To print out the elements by lines using READLINE() function
employee_file = open("employees", "r")

print(employee_file.readline())      # print 1st line
print(employee_file.readline())      # print 2nd line
print(employee_file.readline())      # print 3rd line

employee_file.close()


# If we don't want gap between the lines
employee_file = open("employees", "r")
print(employee_file.readline(), end="")
print(employee_file.readline(), end="")


# To print out all lines at once using READLINES() function and store them in a lists
employee_file = open("employees", "r")

print(employee_file.readlines())

employee_file.close()


# Tp print a specific element/line using index function
employee_file = open("employees", "r")

print(employee_file.readlines()[4])      # 4th index of a list (READLINES)

employee_file.close()


# Using for loop to print out all elements
employee_file = open("employees", "r")

for employee in employee_file.readlines():    # For every variable in list of employee_file
    print(employee, end="")

employee_file.close()


# to create new file, just set a new variable and open them with write function
newfile = open("newfile.txt", "w")
