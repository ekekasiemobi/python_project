def print_matrix_integer(matrix=[[]]):
    for items in matrix:
        item_count = len(items)
        for item in range(item_count):
            print("{:d}".format(items[item]), end="")
            if item < item_count - 1:
                print(" ", end="")
        print("")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
