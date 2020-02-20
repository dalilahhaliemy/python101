name = input("Enter your name:")
age = input("Enter your age:")

print("Hello " + name + "!. You are " + age)


num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = int(num1) + float(num2)
print(result)


# say we only want to take specific index only from the input
second_letter = input("Enter your name: ")[1]     # means we only assigning 2nd letter to the variable
print(second_letter)
