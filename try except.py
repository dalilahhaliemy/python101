# To catch an exception or an error when we run the codes
number = int(input("First try. Enter a number: "))   # If user input letters, it will throw error as in cant convert to integer
print(number)


# We want to specify the error without failing the whole file
try:
    number = int(input("Second tries. Enter a number: "))
    print(number)

except:
    print("Invalid input")         # for all error, it will print this

value = 10/1

# We want to specify errors since below is too general
try:
    value = 10/1
    number = int(input("Third tries. Enter a number: "))
    print(number)

except ValueError:
    print("Invalid input")

except ZeroDivisionError:
    print("Divided by zero")


# While true
# This way, it wont stop asking until user input the correct one. Thus we dont need to manually keep running the function
while True:          # loop gonna keep looping until it hits True
    try:
        number = int(input("Fourth tries. Enter a number: "))
        break        # check for below lines after executing above function. if we don't have this, it wont stop even though user satify the function
    except ValueError:
        print("\nInvalid input. Try again\n")


# Catching the exception name
try:
    print(1/0)
except Exception as exp:
    print("Exception name is: ", exp)


# FINALLY statement
# this is to run the statement regardless if we have exception or not
try:
    print("Resource Open")
    print(1/0)

except Exception as exp:
    print("Exception name is: ", exp)

finally:
    print("Resource Closed")         # we will execute these lines regardless if we run to exception or not
