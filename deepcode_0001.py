def matrix_dot_vector(a:list[list[int|float]], b:list[int|float])-> list[int|float]:
    if len(a[0]) != len(b):
            return -1
        
    vals = []
    for j in range(len(a)):
        hold = 0
        for i in range(len(a[0])): # len(b) == len(a[0])
            hold += a[j][i] * b[i]
        vals.append([hold])
            
    return vals


print(matrix_dot_vector(a = [[1,2],[2,4]], b = [1,2]))

# reasoning: 1*1 + 2*2 = 5;
#             1*2+ 2*4 = 10