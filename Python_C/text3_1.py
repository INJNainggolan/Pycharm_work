#print(float((10 +99j).imag))
'''
from math import *
print(isclose(3, 3))
print(pow(3, 4))
print(3 ** 4)
'''
import math
dayup = math.pow((1.0 + 0.001), 365)
daydown = math.pow((1.0 - 0.001), 365)
print("向上：{:.2f}, 向下：{:.2f}.".format(dayup,daydown))