import numpy as np


def make_diagonal(x):
    x: np.array = np.array([1, 2, 3])
    l = np.size(x)

    result = np.zeros((l, l))

    for i in range(l):
        result[i][i] = x[i]

    print(result)


make_diagonal([1, 2, 3])
