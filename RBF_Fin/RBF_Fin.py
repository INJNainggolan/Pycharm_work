###  RBF_Fin
###
###  Created by 许玥 on 2018/01/10.
###  Copyright © 2018年 许玥. All rights reserved.
###
###  Compiler_environment Python3.6
###  IDE Pycharm 2017.3

from scipy import *
from scipy.linalg import norm, pinv
from matplotlib import pyplot as plt

class RBF:

    def __init__(self, indim, numCenters, outdim):
        self.indim = indim
        self.outdim = outdim
        self.numCenters = numCenters
        self.centers = [random.uniform(-1, 1, indim) for i in range(numCenters)]
        self.beta = 8
        self.W = random.random((self.numCenters, self.outdim))

    def _basisfunc(self, c, d):
        assert len(d) == self.indim
        return exp(-self.beta * norm(c - d) ** 2)

    def _calcAct(self, X):
        # calculate activations of RBFs
        G = zeros((X.shape[0], self.numCenters), float)
        for ci, c in enumerate(self.centers):
            for xi, x in enumerate(X):
                G[xi, ci] = self._basisfunc(c, x)
        return G

    def train(self, X, Y):
        ### X: 维度n X的矩阵
        ### y: n x 1的列向量

        # 从训练集中选择随机的中心矢量
        rnd_idx = random.permutation(X.shape[0])[:self.numCenters]
        self.centers = [X[i, :] for i in rnd_idx]

        print("center", self.centers)
        # 计算激活函数rbf
        G = self._calcAct(X)
        print(G)

        # 计算输出权重
        self.W = dot(pinv(G), Y)

    def test(self, X):

        G = self._calcAct(X)
        Y = dot(G, self.W)
        return Y


if __name__ == '__main__':
    n = 100
    x = mgrid[-1:1:complex(0, n)].reshape(n, 1)
    # 设置y并添加随机噪声
    y = exp((-(x-1)**2)/8)

    # rbf 回归
    rbf = RBF(1, 10, 1)
    rbf.train(x, y)
    z = rbf.test(x)

    # 绘制原始数据
    plt.figure(figsize=(12, 8))
    plt.plot(x, y, 'k-')

    # 绘制学习模型
    plt.plot(x, z, 'r-', linewidth=2)

    # 绘制rbfs
    plt.plot(rbf.centers, zeros(rbf.numCenters), 'gs')

    for c in rbf.centers:

        cx = arange(c - 1, c + 1, 0.005)
        cy = [rbf._basisfunc(array([cx_]), array([c])) for cx_ in cx]
        plt.plot(cx, cy, '-', color='gray', linewidth=0.2)

    plt.xlim(-1.5, 1.5)
    plt.show()