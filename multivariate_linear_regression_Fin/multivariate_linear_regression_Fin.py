import numpy as np
from numpy.linalg import inv
import math
import random

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
    # 生成随机数
    # y = 3.5 * x1 + 3.4 * x2 + 4
    k = 5

    p = [0, 0, 0, 0, 0]
    q = [0, 0, 0, 0, 0]
    s = [0, 0, 0, 0, 0]
    for i in range(k):
        p[i] = random.uniform(50, 100)
        q[i] = random.uniform(10, 30)
        s[i] = 3.5 * p[i] + 3.4 * q[i] + 4
    '''
    for i in range(k):
        print(p[i])
        print(q[i])
        print(s[i])
    print('\n')
    '''

    np.savetxt('X1.csv', p, delimiter=',')
    np.savetxt('X2.csv', q, delimiter=',')
    np.savetxt('Y.csv', s, delimiter=',')
    '''
    x1 = np.loadtxt(open("X1.csv", "rb"), delimiter=",", skiprows=0)
    x2 = np.loadtxt(open("X2.csv", "rb"), delimiter=",", skiprows=0)
    y = np.loadtxt(open("Y.csv", "rb"), delimiter=",", skiprows=0)
    '''


    x = np.transpose(np.vstack((p, q)))
    y = np.matrix([s[0],s[1], s[2], s[3], s[4]], dtype=np.float64).T

    print("****训练样本****")
    print('x:')
    print(x)
    print("y:")
    print(y)
    #多元线性回归模型
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

    l = [0, 0, 0, 0, 0]
    m = [0, 0, 0, 0, 0]
    n = [0, 0, 0, 0, 0]
    for i in range(k):
        l[i] = random.uniform(50, 100)
        m[i] = random.uniform(10, 30)
        n[i] = 3.5 * l[i] + 3.4 * m[i] + 4
    '''
    for i in range(k):
        print(l[i])
        print(m[i])
        print(n[i])
    print('\n')
    '''

    x_text = np.transpose(np.vstack((l, m)))
    y_text = np.matrix([n[0], n[1], n[2], n[3], n[4]], dtype=np.float64).T

    print("****测试样本****")
    print('x_text:')
    print(x_text)
    print("y_text:")
    print(y_text)

    #相关系数、偏相关系数、复相关系数
    print('****相关系数、偏相关系数、复相关系数****')
    correlation_index(x_text, y_text, w)

main()