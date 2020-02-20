# map functions to a list

income = [10, 30, 75]


def double_money(dollars):
    return dollars*2


new_income = list(map(double_money, income))
print(new_income)


for item in income:
    new_income = item*2
    print(new_income)




