# -*- coding: utf-8 -*-
# 最小二乘法，多变量线性回归
import numpy as np
from numpy.linalg import inv
x = np.matrix([[90, 2, 3], [3, 7, 17], [20, 3, 5]], dtype=np.float64)
y = np.matrix([28, 4, 44], dtype=np.float64).T
b = (x.T * x).I * x.T * y
print(x)
print(y)
print(u"参数项矩阵为{0}".format(b))
i = 0
cb = []
while i < 3:
    cb.append(b[i, 0])
    i += 1
temp_e = y - x * b
mye = temp_e.sum() / temp_e.size
e = np.matrix([mye, mye, mye]).T
print("%f*x1+%f*x2+%f*x3+%f" % (cb[0], cb[1], cb[2], mye))
print('!!!!')

x = np.insert(x, 2, axis=1, values=1)
XT = np.transpose(x)
XXT = np.dot(XT, x)
XXTi = inv(XXT)
w = np.dot(XXTi, XT)
W = np.dot(w, y)
print(W)