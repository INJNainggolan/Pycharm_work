import numpy as np
from numpy.linalg import inv
import pandas as pd
import csv
import math

'''
def multivariate_linear_regression(x, y):
    X = np.insert(x, 2, axis=1, values=1)  # 最后一个元素恒置为1
    print("X:\n", X)
    X_mat_trans = np.transpose(X)  # 矩阵转置
    print("X_mat_trans:\n", X_mat_trans)
    X_mat_trans_dot_X = np.dot(X_mat_trans, X)  # 矩阵相乘
    print("X_dot_X_mat_trans:\n", X_mat_trans_dot_X)
    X_dot_X_mat_trans_inv = inv(X_mat_trans_dot_X)  # 矩阵求逆
    print("X_dot_X_mat_trans_inv:\n", X_dot_X_mat_trans_inv)
    XdXmti_dot_Xmt = np.dot(X_dot_X_mat_trans_inv, X_mat_trans)  # 矩阵相乘
    w = np.dot(XdXmti_dot_Xmt, y)  # 矩阵相乘
    print("w:\n", w.T)
    print("y = (%f)*x1+(%f)*x2+(%f)" % (w[0, :], w[1, :], w[2, :]))
'''


def correlation_index(x, y, w):
    #Y 与 X1的相关系数R_YX1
    sum_X1Y = (x[0, 0] * y[0, 0]) + (x[1, 0] * y[1, 0]) + (x[2, 0] * y[2, 0]) \
              + (x[3, 0] * y[3, 0])+ (x[4, 0] * y[4, 0])
    x1_pow_sum_sqrt = math.sqrt(math.pow(x[0, 0], 2) + math.pow(x[1, 0], 2) + math.pow(x[2, 0], 2) \
          + math.pow(x[3, 0], 2) + math.pow(x[4, 0], 2))
    y_pow_sum_sqrt = math.sqrt(math.pow(y[0, 0], 2) + math.pow(y[1, 0], 2) + math.pow(y[2, 0], 2) \
                                + math.pow(y[3, 0], 2) + math.pow(y[4, 0], 2))
    R_YX1 = sum_X1Y/(x1_pow_sum_sqrt * y_pow_sum_sqrt)
    print('Y 与 X1的相关系数R_YX1：', R_YX1)

    #Y 与 X2的相关系数R_YX2
    sum_X2Y = (x[0, 1] * y[0, 0]) + (x[1, 1] * y[1, 0]) + (x[2, 1] * y[2, 0]) \
              + (x[3, 1] * y[3, 0]) + (x[4, 1] * y[4, 0])
    x2_pow_sum_sqrt = math.sqrt(math.pow(x[0, 1], 2) + math.pow(x[1, 1], 2) + math.pow(x[2, 1], 2) \
                                + math.pow(x[3, 1], 2) + math.pow(x[4, 1], 2))
    R_YX2 = sum_X2Y / (x2_pow_sum_sqrt * y_pow_sum_sqrt)
    print('Y 与 X2的相关系数R_YX2：', R_YX1)

    #X1 与 X2的相关系数R_X1X2
    sum_X1X2 = (x[0, 0] * x[0, 1]) + (x[1, 0] * x[1, 1]) + (x[2, 0] * x[2, 1]) \
              + (x[3, 0] * x[3, 1])+ (x[4, 0] * x[4, 1])
    R_X1X2 = sum_X1X2/(x1_pow_sum_sqrt * x2_pow_sum_sqrt)
    print('X1 与 X2的相关系数R_X1X2:', R_X1X2)

    #当X2保持不变时，Y与X1之间的偏相关系数R_YX1_X2
    R_YX1_X2 = (R_YX1 - (R_YX2 * R_X1X2))/(math.sqrt((1 - math.pow(R_YX2, 2)) * (1 - math.pow(R_X1X2, 2))))
    print('当X2保持不变时，Y与X1之间的偏相关系数R_YX1_X2:', R_YX1_X2)

    # 当X1保持不变时，Y与X2之间的偏相关系数R_YX2_X1
    R_YX2_X1 = (R_YX2 - (R_YX1 * R_X1X2)) / (math.sqrt((1 - math.pow(R_YX1, 2)) * (1 - math.pow(R_X1X2, 2))))
    print('当X1保持不变时，Y与X2之间的偏相关系数R_YX2_X1:', R_YX2_X1)

    # 当Y保持不变时，X1与X2之间的偏相关系数R_X1X2_Y
    R_X1X2_Y = (R_X1X2 - (R_YX1 * R_YX2)) / (math.sqrt((1 - math.pow(R_YX1, 2)) * (1 - math.pow(R_YX2, 2))))
    print('当Y保持不变时，X1与X2之间的偏相关系数R_X1X2_Y', R_X1X2_Y)

    #复相关系数R_YX1X2_mul
    Y_ave = (y[0, 0] + y[1, 0] + y[2, 0] + y[3, 0] + y[4, 0])/5
    y0 = w[0, :] * x[0, 0] + w[1, :] * x[0, 1] + w[2, :]
    y1 = w[0, :] * x[1, 0] + w[1, :] * x[1, 1] + w[2, :]
    y2 = w[0, :] * x[2, 0] + w[1, :] * x[2, 1] + w[2, :]
    y3 = w[0, :] * x[3, 0] + w[1, :] * x[3, 1] + w[2, :]
    y4 = w[0, :] * x[4, 0] + w[1, :] * x[4, 1] + w[2, :]
    R_YX1X2_mul = math.sqrt((math.pow(y0 - Y_ave, 2) + math.pow(y1 - Y_ave, 2)\
                                  + math.pow(y2 - Y_ave, 2) + math.pow(y3 - Y_ave, 2)\
                                  + math.pow(y4 - Y_ave, 2))/(math.pow(y[0, 0] - Y_ave, 2)\
                                                              + math.pow(y[1, 0] - Y_ave, 2)\
                                                              + math.pow(y[2, 0] - Y_ave, 2)\
                                                              + math.pow(y[3, 0] - Y_ave, 2)\
                                                              + math.pow(y[4, 0] - Y_ave, 2)))
    print('复相关系数R_YX1X2_mul:', R_YX1X2_mul)

def main():
    '''
    data = pd.read_csv('out.csv', header=None)
    print(data)
    x = pd.read_csv('out.csv', usecols=[0, 1])
    y = pd.read_csv('out.csv', usecols=[2])
    print('x:\n')
    print(x)
    print("y:\n")
    print(y)
    '''
    x = np.matrix([[3, 5], [1, 4], [5, 6], [2, 4], [4, 6]], dtype=np.float64)
    y = np.matrix([3, 1, 8, 3, 5], dtype=np.float64).T
    print('x:\n')
    print(x)
    print("y:\n")
    print(y)
    #multivariate_linear_regression(x, y)

    X = np.insert(x, 2, axis=1, values=1)  # 最后一个元素恒置为1
    print("X:\n", X)
    X_mat_trans = np.transpose(X)  # 矩阵转置
    print("X_mat_trans:\n", X_mat_trans)
    X_mat_trans_dot_X = np.dot(X_mat_trans, X)  # 矩阵相乘
    print("X_dot_X_mat_trans:\n", X_mat_trans_dot_X)
    X_dot_X_mat_trans_inv = inv(X_mat_trans_dot_X)  # 矩阵求逆
    print("X_dot_X_mat_trans_inv:\n", X_dot_X_mat_trans_inv)
    XdXmti_dot_Xmt = np.dot(X_dot_X_mat_trans_inv, X_mat_trans)  # 矩阵相乘
    w = np.dot(XdXmti_dot_Xmt, y)  # 矩阵相乘
    print("w:\n", w.T)
    print("y = (%f)*x1+(%f)*x2+(%f)" % (w[0, :], w[1, :], w[2, :]))

    correlation_index(x, y, w)

main()
