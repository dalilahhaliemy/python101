# building calculator with operations +-*/

num1 = float(input("Enter first number: "))    # use float to convert string to number (allowing decimals)
op = input("Enter operator. Choose between + = / * : ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1/num2)
elif op == "*":
    print(num1*num2)
else:
    print("Invalid operator")
