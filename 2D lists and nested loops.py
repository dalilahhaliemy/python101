# say we wanna print a 2D lists

test = [1, 2, 3]
print(test)     # can simply print 1D lists

number_grid = [
    [1, 2, 3],       # row 1 has 3 column, 1st list
    [4, 5, 6],       # row 2, 2nd list
    [7, 8, 9],       # row 3, 3rd list
    [0]              # row 4, 4th list
]

# we cant simply print all elements using print(number_grid). It will throw error since it is a 2D lists
# printing specific element using coordinate
print(number_grid[0][0])     # [row][col]


# print lists by rows using for loop
for row in number_grid:
    print(row)               # printing all row 1-4


# print each column in a specific row to get all element
# looping in a loop (multiple loops/nested loops)
for row in number_grid:
    for col in row:
        print(col)           # printing each col in a row
