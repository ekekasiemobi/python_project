#!/usr/bin/python3
print_sorted_dictionary = \
    __import__('6-task').print_sorted_dictionary
def multiply_by_2(a_dictionary):
    new_dict = {}
    for i in a_dictionary.items():
        new_dict.update({i[0]: i[1] * 2})
    return new_dict

a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
new_dict = multiply_by_2(a_dictionary)
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)
