# a WHILE LOOP will “do” something as long as or until a condition is met.
# in other words, until a condition is met, run the loop
# say we want to loop 10 times
# ALWAYS start with empty variable
'''
i = 1
while i <= 10:           # as long as this condition is met, we gonna keep looping
    print(i)
    i = i + 1

print("Done with loop")

# NESTED WHILE LOOP
# say we want to print below. we can use nested while loop
#   Didi rocks rocks rocks rocks
#   Didi rocks rocks rocks rocks
#   Didi rocks rocks rocks rocks
#   Didi rocks rocks rocks rocks
#   Didi rocks rocks rocks rocks

i = 1

while i <= 5:
    j = 1
    print("Didi ", end="")        # print on same line
    while j <= 4:
        print("rocks ", end="")   # print 4 rocks on same line as 1 Didi
        j += 1
    i += 1
    print()                       # now print on new line, repeat the loop for 2nd Didi


# another example

i = 1
while i <= 5:
    print("*" * i)
    i += 1
print("Done")


secret_num = 9
counter = 1

while counter <= 3:
    guess = int(input("Enter guess : "))
    counter += 1
    if guess == secret_num:
        print("You win")
        break
else:
    print("You lose")
'''

# another example
command = ""
started = False
while True: # command != "quit
    command = input(">")

    if command == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")

    elif command == "start":
        if started:
            print("Car already started")
        else:
            print("Car started... Lets go")
            started = True

    elif command == "stop":
        if not started:
            print("Already stopped")
        else:
            print("Stopped")
            started = False

    elif command == "quit":
        break
    else:
        print("I don't understand")
