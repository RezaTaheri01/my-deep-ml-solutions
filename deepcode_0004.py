def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if not matrix:
        return 0
    
    r, c = len(matrix), len(matrix[0])  
    means: list[float] = [] 
    
    for j in range(r):
        _sum = 0
        for i in range(c):
            _sum += matrix[j][i] if mode == 'row' else matrix[i][j]
        means.append(_sum / c)
        
    return means


print(calculate_matrix_mean(matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], mode = 'row'))