def transpose_matrix(a: list[list[int | float]]) -> list[list[int | float]]:
    if not a:
        return []
    
    r, c = len(a), len(a[-1])

    result: list[list[int | float]] = [[0 for _ in range(r)] for _ in range(c)]

    for i in range(r):
        for j in range(c):
            result[j][i] = a[i][j]
            
    return result


print(transpose_matrix([[1,2,3],[4,5,6]]))


# input: a = [[1,2,3],[4,5,6]]
# output: [[1,4],[2,5],[3,6]]
