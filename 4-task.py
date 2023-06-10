def new_in_list(my_list, idx, element):
    list_count = len(my_list)
    if idx < 0:
        return my_list
    if idx > list_count:
        return my_list
    else:
        my_list[idx] = element
        return my_list


my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)