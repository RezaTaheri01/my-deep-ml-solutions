def scalar_multiply(matrix: list[list[int | float]], scalar: int | float) -> list[list[int | float]]:
    return [[element * scalar for element in row] for row in matrix]


print(scalar_multiply(matrix=[[1, 2], [3, 4]], scalar=2))
