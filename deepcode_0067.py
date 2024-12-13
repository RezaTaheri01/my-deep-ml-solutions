def compressed_col_sparse_matrix(dense_matrix):
    values = []
    row_indexes = []
    col_pointer = [0]

    for i in range(len(dense_matrix[0])):
        for j in range(len(dense_matrix)):
            if dense_matrix[j][i] != 0:
                values.append(dense_matrix[j][i])
                row_indexes.append(j)
        col_pointer.append(len(row_indexes))

    return values, row_indexes, col_pointer


print(compressed_col_sparse_matrix(dense_matrix=[
    [0, 0, 3, 0],
    [1, 0, 0, 4],
    [0, 2, 0, 0]
]))
