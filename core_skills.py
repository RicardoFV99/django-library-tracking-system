import random
rand_list = [2, 4, 5, 7, 2, 34, 23, 8, 9 , 17]
list_comprehension_below_10 = []

#using for
for x in rand_list:
    if x < 10:
        list_comprehension_below_10.append(x)

print(f"Using for: {list_comprehension_below_10}")

#using filter method
list_comprehension_below_10 = []
def below_10_func(x):
    if x < 10:
        return True
    else:
        return False

list_comprehension_below_10 = list(filter(below_10_func, rand_list))

print(f"Using filter method: {list_comprehension_below_10}")