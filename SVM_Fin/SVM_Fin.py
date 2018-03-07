###  SVM_Fin
###
###  Created by 许玥 on 2018/01/10.
###  Copyright © 2018年 许玥. All rights reserved.
###
###  Compiler_environment Python3.6
###  IDE Pycharm 2017.3

from numpy import *
import random
import matplotlib.pyplot as plt

def data():
    dataSet = []
    labels = []
    dataSet_I = [[0 for i in range(2)] for i in range(50)]
    dataSet_II = [[0 for i in range(2)] for i in range(50)]
    for i in range(50):
        data_I = random.uniform(-12, -1)
        data_II = random.uniform(-12, 0)
        dataSet_I[i][0] = data_I
        dataSet_I[i][1] = data_II
    for j in range(50):
        data_I = random.uniform(-1, 12)
        data_II = random.uniform(6, 12)
        dataSet_II[j][0] = data_I
        dataSet_II[j][1] = data_II
    dataSet = dataSet_I + dataSet_II
    labels_I = [0 for i in range(50)]
    labels_II = [0 for i in range(50)]
    for i in range(50):
        data_III = 1
        labels_I[i] = data_III
    for j in range(50):
        data_III = -1
        labels_II[j] = data_III
    labels = labels_I + labels_II

    return dataSet, labels

# 计算核函数
def calcKernelValue(matrix_x, sample_x, kernelOption):
    kernelType = kernelOption[0]
    numSamples = matrix_x.shape[0]
    kernelValue = mat(zeros((numSamples, 1)))

    if kernelType == 'linear':
        kernelValue = matrix_x * sample_x.T
    elif kernelType == 'rbf':
        sigma = kernelOption[1]
        if sigma == 0:
            sigma = 1.0
        for i in range(numSamples):
            diff = matrix_x[i, :] - sample_x
            kernelValue[i] = exp(diff * diff.T / (-2.0 * sigma ** 2))
    else:
        raise NameError('不支持内核类型!你可以使用线性或rbf！')
    return kernelValue


# 计算给定训练集和内核类型的内核矩阵
def calcKernelMatrix(train_x, kernelOption):
    numSamples = train_x.shape[0]
    kernelMatrix = mat(zeros((numSamples, numSamples)))
    for i in range(numSamples):
        kernelMatrix[:, i] = calcKernelValue(train_x, train_x[i, :], kernelOption)
    return kernelMatrix


# 定义一个用于存储变量和数据的结构体
class SVMStruct:
    def __init__(self, dataSet, labels, C, toler, kernelOption):
        self.train_x = dataSet  # 每一行代表一个样本
        self.train_y = labels  # 相应的标签
        self.C = C  # 松弛变量
        self.toler = toler  # 迭代终止条件
        self.numSamples = dataSet.shape[0]  # 样例的数量
        self.alphas = mat(zeros((self.numSamples, 1)))  # 所有样本的拉格朗氏因子
        self.b = 0
        self.errorCache = mat(zeros((self.numSamples, 2)))
        self.kernelOpt = kernelOption
        self.kernelMat = calcKernelMatrix(self.train_x, self.kernelOpt)


# 计算alpha k的误差
def calcError(svm, alpha_k):
    output_k = float(multiply(svm.alphas, svm.train_y).T * svm.kernelMat[:, alpha_k] + svm.b)
    error_k = output_k - float(svm.train_y[alpha_k])
    return error_k


# 在优化阿尔法k之后，更新alpha k的错误缓存
def updateError(svm, alpha_k):
    error = calcError(svm, alpha_k)
    svm.errorCache[alpha_k] = [1, error]


# alpha j
def selectAlpha_j(svm, alpha_i, error_i):
    svm.errorCache[alpha_i] = [1, error_i]  # mark as valid(has been optimized)
    candidateAlphaList = nonzero(svm.errorCache[:, 0].A)[0]  # mat.A return array
    maxStep = 0
    alpha_j = 0
    error_j = 0

    # 用最大的迭代步骤找到阿尔法
    if len(candidateAlphaList) > 1:
        for alpha_k in candidateAlphaList:
            if alpha_k == alpha_i:
                continue
            error_k = calcError(svm, alpha_k)
            if abs(error_k - error_i) > maxStep:
                maxStep = abs(error_k - error_i)
                alpha_j = alpha_k
                error_j = error_k
    # 如果第一次出现在这个循环中，我们会随机选择alpha j
    else:
        alpha_j = alpha_i
        while alpha_j == alpha_i:
            alpha_j = int(random.uniform(0, svm.numSamples))
        error_j = calcError(svm, alpha_j)

    return alpha_j, error_j


# 优化阿尔法i和alpha j的内部循环
def innerLoop(svm, alpha_i):
    error_i = calcError(svm, alpha_i)

    if (svm.train_y[alpha_i] * error_i < -svm.toler) and (svm.alphas[alpha_i] < svm.C) or \
            (svm.train_y[alpha_i] * error_i > svm.toler) and (svm.alphas[alpha_i] > 0):

        # 步骤1：选择alpha j
        alpha_j, error_j = selectAlpha_j(svm, alpha_i, error_i)
        alpha_i_old = svm.alphas[alpha_i].copy()
        alpha_j_old = svm.alphas[alpha_j].copy()

        # 步骤2: 计算阿尔法j的边界L和H
        if svm.train_y[alpha_i] != svm.train_y[alpha_j]:
            L = max(0, svm.alphas[alpha_j] - svm.alphas[alpha_i])
            H = min(svm.C, svm.C + svm.alphas[alpha_j] - svm.alphas[alpha_i])
        else:
            L = max(0, svm.alphas[alpha_j] + svm.alphas[alpha_i] - svm.C)
            H = min(svm.C, svm.alphas[alpha_j] + svm.alphas[alpha_i])
        if L == H:
            return 0

        # 步骤3: 计算eta(样本i和j的相似性)
        eta = 2.0 * svm.kernelMat[alpha_i, alpha_j] - svm.kernelMat[alpha_i, alpha_i] \
              - svm.kernelMat[alpha_j, alpha_j]
        if eta >= 0:
            return 0

        # 步骤4: 更新alphaj
        svm.alphas[alpha_j] -= svm.train_y[alpha_j] * (error_i - error_j) / eta

        # 步骤5:剪辑alpha j
        if svm.alphas[alpha_j] > H:
            svm.alphas[alpha_j] = H
        if svm.alphas[alpha_j] < L:
            svm.alphas[alpha_j] = L

        # 第6步: 如果阿尔法j移动不够，就返回
        if abs(alpha_j_old - svm.alphas[alpha_j]) < 0.00001:
            updateError(svm, alpha_j)
            return 0

        #步骤7: 在优化aiphaj之后更新alpha
        svm.alphas[alpha_i] += svm.train_y[alpha_i] * svm.train_y[alpha_j] \
                               * (alpha_j_old - svm.alphas[alpha_j])

        # 步骤8:更新阈值b
        b1 = svm.b - error_i - svm.train_y[alpha_i] * (svm.alphas[alpha_i] - alpha_i_old) \
             * svm.kernelMat[alpha_i, alpha_i] \
             - svm.train_y[alpha_j] * (svm.alphas[alpha_j] - alpha_j_old) \
             * svm.kernelMat[alpha_i, alpha_j]
        b2 = svm.b - error_j - svm.train_y[alpha_i] * (svm.alphas[alpha_i] - alpha_i_old) \
             * svm.kernelMat[alpha_i, alpha_j] \
             - svm.train_y[alpha_j] * (svm.alphas[alpha_j] - alpha_j_old) \
             * svm.kernelMat[alpha_j, alpha_j]
        if (0 < svm.alphas[alpha_i]) and (svm.alphas[alpha_i] < svm.C):
            svm.b = b1
        elif (0 < svm.alphas[alpha_j]) and (svm.alphas[alpha_j] < svm.C):
            svm.b = b2
        else:
            svm.b = (b1 + b2) / 2.0

        # 步骤9:在优化阿尔法i j和b之后，为alpha i更新错误缓存
        updateError(svm, alpha_j)
        updateError(svm, alpha_i)

        return 1
    else:
        return 0


# 训练SVM
def trainSVM(train_x, train_y, C, toler, maxIter, kernelOption=('rbf', 1.0)):

    # 初始化svm数据结构
    svm = SVMStruct(mat(train_x), mat(train_y), C, toler, kernelOption)

    # 开始训练
    entireSet = True
    alphaPairsChanged = 0
    iterCount = 0
    # 迭代终止条件:
    # 条件1: 达到最大迭代
    # 条件2: 在遍历所有样本后，没有alpha值发生变化，换句话说，所有阿尔法(样本)都符合KKT条件
    while (iterCount < maxIter) and ((alphaPairsChanged > 0) or entireSet):
        alphaPairsChanged = 0

        # 更新所有训练样本的alphas
        if entireSet:
            for i in range(svm.numSamples):   # numSamples = matrix_x.shape[0]
                alphaPairsChanged += innerLoop(svm, i)
            #print('---iter:%d entire set, alpha pairs changed:%d' % (iterCount, alphaPairsChanged))
            iterCount += 1
        # 更新不是0或者C(不在边界上)的alphas
        else:
            nonBoundAlphasList = nonzero((svm.alphas.A > 0) * (svm.alphas.A < svm.C))[0]
            for i in nonBoundAlphasList:
                alphaPairsChanged += innerLoop(svm, i)
            #print('---iter:%d non boundary, alpha pairs changed:%d' % (iterCount, alphaPairsChanged))
            iterCount += 1

        # 在所有示例和非边界示例中交替循环
        if entireSet:
            entireSet = False
        elif alphaPairsChanged == 0:
            entireSet = True

    return svm


# 给定测试集测试svm
def testSVM(svm, test_x, test_y):
    test_x = mat(test_x)
    test_y = mat(test_y)
    numTestSamples = test_x.shape[0]
    supportVectorsIndex = nonzero(svm.alphas.A > 0)[0]
    supportVectors = svm.train_x[supportVectorsIndex]
    supportVectorLabels = svm.train_y[supportVectorsIndex]
    supportVectorAlphas = svm.alphas[supportVectorsIndex]
    matchCount = 0
    for i in range(numTestSamples):
        kernelValue = calcKernelValue(supportVectors, test_x[i, :], svm.kernelOpt)
        predict = kernelValue.T * multiply(supportVectorLabels, supportVectorAlphas) + svm.b
        if sign(predict) == sign(test_y[i]):
            matchCount += 1
    accuracy = float(matchCount) / numTestSamples
    return accuracy


# 画出训练后的svm模型
def paintSVM(svm):
    if svm.train_x.shape[1] != 2:
        print("sorry!数据维度不是2维!")
        return 1

    # 画出所有样例
    for i in range(svm.numSamples):
        if svm.train_y[i] == -1:
            plt.plot(svm.train_x[i, 0], svm.train_x[i, 1], 'or')
        elif svm.train_y[i] == 1:
            plt.plot(svm.train_x[i, 0], svm.train_x[i, 1], 'ob')

    # 标记支持向量
    supportVectorsIndex = nonzero(svm.alphas.A > 0)[0]
    for i in supportVectorsIndex:
        plt.plot(svm.train_x[i, 0], svm.train_x[i, 1], 'oy')

    # 画出超平面
    w = zeros((2, 1))
    for i in supportVectorsIndex:
        w += multiply(svm.alphas[i] * svm.train_y[i], svm.train_x[i, :].T)
    min_x = min(svm.train_x[:, 0])[0, 0]
    max_x = max(svm.train_x[:, 0])[0, 0]
    y_min_x = float(-svm.b - w[0] * min_x) / w[1]
    y_max_x = float(-svm.b - w[0] * max_x) / w[1]
    plt.plot([min_x, max_x], [y_min_x, y_max_x], '-g')
    plt.show()

if __name__=="__main__":

    dataSet, labels = data()

    dataSet = mat(dataSet)  ###mat函数转换为矩阵
    labels = mat(labels).T  ###mat函数转换为矩阵
    train_x = dataSet[0:81, :]  ###训练集
    train_y = labels[0:81, :]  ###训练集
    test_x = dataSet[80:101, :]  ###测试集
    test_y = labels[80:101, :]  ###测试集

    C = 1.0    #松弛变量，确定上下边界L,H
    toler = 0.005  ###迭代终止条件
    maxIter = 100  ###最大迭代次数
    ###SVM分类器   kernel核函数
    svmClassifier = trainSVM(train_x, train_y, C, toler, maxIter, kernelOption=('linear', 0))

    accuracy = testSVM(svmClassifier, test_x, test_y)
    print('The classify accuracy is: %.3f%%' % (accuracy * 100))

    paintSVM(svmClassifier)   ###画出图像