# search n in a list
# using for loop
list1 = [8, 8, 0, 6, 0, 9]
n1 = 9
position = 1

for i in list1:
    if i == n1:
        print("Found at position ", position)
        break
    else:
        position += 1


# using while loop in a function
# say we wanna know the position
def search(list, n):
    i = 0
    global position
    position = 1

    while i < len(list):      # i range from 0-5 (all 6 elements)

        if list[i] == n:      # if the index is 9, then return True
            return True
        i += 1
        position += 1
    return False


if search(list1, n1):
    print("Found at position ", position)
else:
    print("Not found")

