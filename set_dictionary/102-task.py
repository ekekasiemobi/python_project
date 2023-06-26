#!/usr/bin/python3
print_sorted_dictionary = \
    __import__('6-task').print_sorted_dictionary
def complex_delete(my_dictionary, value):
    del_key = []
    for key in my_dictionary:
        if my_dictionary[key] == value:
            del_key.append(key)
    for key in del_key:
        del my_dictionary[key]
    return my_dictionary


a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}
new_dict = complex_delete(a_dictionary, 'C')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

print("--")
print("--")
new_dict = complex_delete(a_dictionary, 'c_is_fun')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)