# BUBBLE SORT
# sort by checking 5 against all number
# then compare is 5> then the number, if yes, swap
nums = [5, 3, 8, 6, 7, 2]


def sort(list):
    for i in range(len(list)-1, 0, -1):
        for j in range(i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp


sort(nums)
print(nums)


# SELECTIVE SORT
# sort some of the value only, since if we use bubble sort, it will consider all option
nums = [5, 3, 8, 6, 7, 2]


