# ZIP
# say we have 2 list, we wanna tie them together

first = ['Bucky', 'Tom', 'Taylor']
last = ['Roberts', 'Hanks', 'Swift']

names = zip(first, last)    # tie them together in a variable name list

for a, b in names:
    print(a, b)

# now names is actually [(Bucky, Roberts), (Tom, Hanks), (Taylor, Swift)]
# this now become a tuple
print(type(names))


# LAMBDA
# small function that has no name

answer = lambda x: x*7     # nameless function. no need to define a name to the function
print(answer(5))

