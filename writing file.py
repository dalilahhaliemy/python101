# Append data to the file using "a" function
employee_file = open("employees", "a")

employee_file.write("\nToby - Human Resources")

print("Success append")

employee_file.close()


# Change data of the file using "w" function
employee_file = open("employees", "w")

employee_file.write("Jim - Salesman\nDwight - Salesman\nPam - Receptionist\nMicheal - Manager\nOscar - Accountant")   # Replace the whole data with this
print("Write success")

employee_file.close()


# Creating new file
employee1_file = open("employees1.txt", "w")


# Copying 1 file data into another
employee_file = open("employees", "r")
new_file = open("newfile", "w")

for data in employee_file:
    new_file.write(data)
print("Copying success")


# Copying IMAGE
# Image is stored in binary numbers and it can only be read if we store it at another file
old_pic = open("464.jpg", "rb")     # read binary
new_pic = open("NewPic.jpg", "wb")  # store in new file in binary format

for codes in old_pic:
    new_pic.write(codes)            # write the codes in new_pic file

print("Success duplicating")
