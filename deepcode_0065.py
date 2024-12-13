import numpy as np


def compressed_row_sparse_matrix(dense_matrix):
    values = []
    col_indexes = []
    row_pointer = [0]

    for row in dense_matrix:
        for i, val in enumerate(row):
            if val != 0:
                values.append(val)
                col_indexes.append(i)
        row_pointer.append(len(col_indexes))

    return values, col_indexes, row_pointer


print(compressed_row_sparse_matrix(dense_matrix=[
    [1, 0, 0, 0],
    [0, 2, 0, 0],
    [3, 0, 4, 0],
    [1, 0, 0, 5]
]))
