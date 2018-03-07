from numpy import *
import SVM

################## test svm #####################
## step 1: load data

print("step 1: load data...")
dataSet = []
labels = []

fileIn = open('testSet.txt')
for line in fileIn.readlines():
	lineArr = line.strip().split('\t')
	dataSet.append([float(lineArr[0]), float(lineArr[1])])
	labels.append(float(lineArr[2]))


dataSet = mat(dataSet)   ###mat函数转换为矩阵
labels = mat(labels).T   ###mat函数转换为矩阵
train_x = dataSet[0:81, :]   ###训练集
train_y = labels[0:81, :]   ###训练集
test_x = dataSet[80:101, :]   ###测试集
test_y = labels[80:101, :]   ###测试集


## step 2: training...
print("step 2: training...")
C = 0.6
toler = 0.001   ###比例系数
maxIter = 50   ###最大迭代次数
###SVM分类器   kernel核函数
svmClassifier = SVM.trainSVM(train_x, train_y, C, toler, maxIter, kernelOption = ('linear', 0))

## step 3: testing
print("step 3: testing...")
accuracy = SVM.testSVM(svmClassifier, test_x, test_y)

## step 4: show the result
print("step 4: show the result...")
print('The classify accuracy is: %.3f%%' % (accuracy * 100))
SVM.showSVM(svmClassifier)