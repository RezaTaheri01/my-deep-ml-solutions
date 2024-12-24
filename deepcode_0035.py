import numpy as np


def make_diagonal(x):
    x: np.array = np.array(x)
    l = np.size(x)

    result = np.zeros((l, l))

    for i in range(l):
        result[i][i] = x[i]

    print(result)


make_diagonal([1, 2, 3])
make_diagonal([4, 5, 6, 7])

