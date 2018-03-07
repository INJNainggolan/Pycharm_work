# -*- coding: utf-8 -*-

"""
转换图片
"""
import os 
import operator
from os import listdir
from numpy import *
import sys
import importlib
importlib.reload(sys)

"""
将每张图片转换成向量形式
即把每张图片转换成一维1*1024矩阵形式
"""
def img2vector(filename):
    """
    filename代表文件名称
    """
    returnVector = zeros((1,1024))##声明一个0矩阵
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()##°每一行文件
        for j in range(32):
            returnVector[0,32*i+j] = int(lineStr[j])##一共32行，全部存储到returnVector里面
    fr.close()
    return returnVector

def classify0(inX,dataSet,labels,k):
    """
    四个参数，inX是测试向量，dataSet样本向量数据，labels是标签，k是选取前k个做评测
    tile(A,n)用于重复A矩阵n次
    argsort()返回的是数组值从小到大的索引
    list.get(k,d)
    get()相当于一条if...else...语句,参数k在字典中，字典将返回list[k];如果参数k不在字典中则返回参数d,如果K在字典中则返回k对应的value值；
    例子：
    l = {5:2,3:4}
    print l.get(3,0)返回的值是4；
    Print l.get（1,0）返回值是0；(该例来源于网络)
    """
    dataSetSize = dataSet.shape[0]##shpe函数用于返回矩阵的长度，如shape[0]返回第一维矩阵长度，shape[1]返回第二维矩阵长度以此类推，还有其他功能执行查阅
    diffMat = tile(inX,(dataSetSize,1)) - dataSet##tile函数主要功能是重复矩阵多少次，重复了测试向量，与每一个样本相减
    sqDiffMat = diffMat**2##计算平方
    sqDistances = sqDiffMat.sum(axis = 1)##计算矩阵横轴的和
    distances = sqDistances**0.5##平方
    sortedDistIndicies = distances.argsort()##用argsort排序
    classCount = {}
    for i in range(k):
        voteLabel = labels[sortedDistIndicies[i]]##通过索引得到前该距离所属的类型
        classCount[voteLabel] = classCount.get(voteLabel,0)+1##相应的类型+1
    sortedClassCount = sorted(classCount.items(),key = operator.itemgetter(1),reverse = True)
    return sortedClassCount[0][0]

def handwritingClassTest():
    hwLabels = []
    trainingFileList = listdir('trainingDigits')
    m = len(trainingFileList)
    trainingMat = zeros((m, 1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('.')[0])
        hwLabels.append(classNumStr)
        trainingMat[i,:] = img2vector('trainingDigits/%s' % fileNameStr)
    testFileList = listdir('testDigits')
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        print("the classifier came bace with:%d, the real answer is:%d" % (classifierResult, classNumStr))
        if(classifierResult != classNumStr):
            errorCount += 1.0
    print("the total number of errors is: %d" % errorCount)
    print("the total error rate is :%f" % (errorCount/float(mTest)))

if __name__ == '__main__':
    handwritingClassTest()
    print ("测试完成")