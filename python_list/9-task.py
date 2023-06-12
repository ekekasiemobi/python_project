#!/usr/bin/python3
def max_integer(my_list=[]):
    list_count = len(my_list)
    max_value = my_list[0]
    if list_count == 0:
        return None
    for num in my_list:
        if num > max_value:
            max_value = num
    return max_value


my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))