def print_one_loop(matrix):
    if not isinstance(matrix, list):
        return

    if not isinstance(matrix[0], list):
        for elem in matrix:
            print(elem)

    else:    # just assume 2d
        m, n = len(matrix), len(matrix[0])
        for i in range(m * n):
            print(matrix[i // n][i % n])

    print('')

matrix = [[0,1],[2,3],[4,5]]
print_one_loop(matrix)
for m in matrix: print_one_loop(m)