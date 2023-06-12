def no_c(my_string):
    new_string = ""
    for letters in my_string:
        if letters != 'c' and letters != 'C':
            new_string += letters
    return new_string


print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))