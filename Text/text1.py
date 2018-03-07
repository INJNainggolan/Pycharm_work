import numpy as np

x = np.matrix(np.arange(12).reshape((3, 4)))
print(x.A[2])
'''
matrix([[ 0,  1,  2,  3],
        [ 4,  5,  6,  7],
        [ 8,  9, 10, 11]])
'''
