#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    result = []
    for letter in set_1:
        if letter not in set_2:
            result.append(letter)

    for letter in set_2:
        if letter not in set_1:
            result.append(letter)

    return result


set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))