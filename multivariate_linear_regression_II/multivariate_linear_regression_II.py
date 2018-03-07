import numpy as np
import scipy.stats.stats as stats
from numpy import linalg as lstsq
def load_exdata(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            line = line.split(',')
            current = [int(item) for item in line]
            #5.5277,9.1302
            data.append(current)
    return data

data = load_exdata('ex1data2.txt');
data = np.array(data,np.int64)

x1 = data[:, (0)].reshape((-1, 1))
x2 = data[:, (1)].reshape((-1, 1))
x = data[:, (0, 1)].reshape((-1, 2))
y = data[:, 2].reshape((-1, 1))
m = y.shape[0]

# Print out some data points
print('First 10 examples from the dataset: \n')
print(' x1 = ', x1[:, :], '\n')
print(' x2 = ', x2[:, :], '\n')
print(' x = ', x[:, :], '\n')
print('y=', y[:, :])
print(m)




#x=[2,4,5,6,4,7,8,5,6,7]
#y=[3,2,6,5,3,6,5,4,4,5]
#r=stats.pearsonr(x1,y)[0]
#print(r)
#print(lstsq(x1, y)[0])#输出的为β

'''
#from math import sqrt
#import scipy.stats.stats as stats
def multipl(a, b):
    sumofab = 0.0
    for i in range(len(a)):
        temp = a[i] * b[i]
        sumofab += temp
    return sumofab


def corrcoef(x, y):
    n = len(x)
    # 求和
    sum1 = sum(x)
    sum2 = sum(y)
    # 求乘积之和
    sumofxy = multipl(x, y)
    # 求平方和
    sumofx2 = sum([pow(i, 2) for i in x])
    sumofy2 = sum([pow(j, 2) for j in y])
    num = sumofxy - (float(sum1) * float(sum2) / n)
    # 计算皮尔逊相关系数
    den = sqrt((sumofx2 - float(sum1 ** 2) / n) * (sumofy2 - float(sum2 ** 2) / n))
    return num / den


#x = [0, 1, 0, 3]
#y = [0, 1, 1, 1]

print(corrcoef(x, y))  # 0.471404520791
'''