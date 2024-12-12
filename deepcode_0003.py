import numpy as np


def reshape_matrix(a: list[list[int | float]], new_shape: tuple[int, int]) -> list[list[int | float]]:
    if not a:
        return a

    if len(a) * len(a[0]) != new_shape[0] * new_shape[1]:
        return -1
    
    return np.reshape(a, new_shape).tolist()


print(reshape_matrix(a=[[1, 2, 3, 4], [5, 6, 7, 8]], new_shape=(4, 2)))


# region raw code
# def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
# 	#Write your code here and return a python list after reshaping by using numpy's tolist() method
#     if not a:
#         return a

#     r, c = len(a), len(a[0])
#     new_r, new_c = new_shape

#     if r * c != new_r * new_c:
#         return -1

#     result: list[list[float]] = []
#     temp: list[float] = []
#     counter: int = 0

#     for j in range(r):
#         for i in range(c):
#             counter += 1
#             temp.append(a[j][i])

#             if counter == new_c:
#                 result.append(temp)
#                 counter = 0
#                 temp = []

#     return result
# endregion
