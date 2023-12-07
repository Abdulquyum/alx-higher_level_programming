def square_matrix_simple(matrix=[]):
    sqr = []
    for x in matrix:
        z = [y ** 2 for y in x]
        sqr.append(z)
    return sqr
