# 空气质量提醒
'''
def main():
    PM = eval(input("What is today's PM2.5?'"))
    if PM > 75:
        print("Unhealthy.Be careful!")
    if PM < 35:
        print("Good. Go running!")
main()
'''

#计算二次方程的实数根程序
#此程序在方程没有实根的情况下报错
'''
import math
def main():
    print("This program finds the real solutions to a quadratic\n")
    a, b, c = eval(input ("Please enter the coefficients(a, b, c):\n"))
    discRoot = math.sqrt(b * b - 4 * a * c)
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)
    print("\nThe Root1 is:",root1,"\nThe Root2 is:",root2)
main()
'''

#计算二次方程的实数根程序
#当a赋值为0时，会报错，因为被除数不能为0
'''
import math
def main():
    print("Let us finds the solutions to a quadratic\n")
    a, b, c = eval(input("Do enter thr coefficients (a, b, c):\n"))
    delta = b * b - 4 * a * c
    if delta < 0:
        print("\nThe equation has no real roots!")
    elif delta == 0:
        x = -b /(2 *a)
        print("\nThere is a double root at",x)
    else:
        discRoot = math.sqrt(delta)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print("\nThe Root1 is:",root1,"\nThe Root2 is:",root2)
main()
'''

#计算二次方程的实数根程序
#改进上述程序
'''
import math
def main():
    print("Let us finds the solutions to a quadratic\n")
    a, b, c = eval(input("Do enter thr coefficients (a, b, c):\n"))
    delta = b * b - 4 * a * c
    if a == 0:
        root = -b / c
        print("\nThere is an solution",root)
    elif delta < 0:
        print("\nThe equation has no real roots!")
    elif delta == 0:
        root = -b /(2 *a)
        print("\nThere is a double root at",root)
    else:
        discRoot = math.sqrt(delta)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print("\nThe Root1 is:",root1,"\nThe Root2 is:",root2)
main()
'''

#计算二次方程的实数根程序
#带错误处理的的程序
'''
import math
def main():
    print("This program finds the real solutions to a quadratic\n")
    try:
        a, b, c = input("Please enter the coefficients (a, b, c):")
        discRoot = math.sqrt(b * b - 4 * a *c)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print("\nThe solutions are :", root1, root2)
    except ValueError:
        print("\nNo real roots")
main()
'''

#寻找一组数中的最大值
'''
def main():
    n = eval(input("How many numbers are there?"))
    #将第一个数赋值给max
    max = eval(input("Enter a number >>"))
    #连续与后面n-1个数字进行比较
    for i in range(n - 1):
        x = eval(input("Enter a number >>"))
        if x > max:
            max = x
        print("The largest value is :",max)
main()
'''

#使用Python内置的max函数搞定最大值问题
'''
def main():
    x1, x2, x3 = eval(input("Please enter three values:"))
    print("The largest value is",max(x1, x2, x3)) 
main()
'''

#求平均数
'''
def main():
    n = eval(input("How many numbers？"))
    sum = 0.0
    for i in range(n):
        x = eval(input("Enter a number >>"))
        sum = sum + x
    print("\nThe average is",sum / n)
main()
'''

'''
def main():
    i = 0
    while i <= 10:
        print(i)
        i = i + 1
main()
'''

'''
def main():
    sum = 0
    number = 0
    while number < 20:
        number += 1
        sum += number
        if sum > 100:
            break
    print("The number is ",number)
    print("The sum is ",sum)
main()
'''

'''
def main():
    for n in range(2,10):
        for x in range(2,n):
            if n % x == 0:
                print(n,'equals',x,'*',n//x)#用于浮点数除法,其结果进行四舍五入
                break
        else:
            print(n,'is a prime number')
main()
'''

'''
def main():
    sum = 0.0
    count = 0
    moredata = "yes"
    while moredata[0] == "y":
        x = eval(input("Enter a number >> "))
        sum = sum + x
        count = count + 1
        moredata = input("Do you have more numbers (yes or no)?")
    print("\nThe average of the numbers is ",sum/count)
main()
'''

'''
def main():
    print("Hello World")
main()
'''

'''
if __name__ == "__main__":
    print("Hello World")
'''

'''
import py_compile
py_compile.compile('hello.py')
'''

'''
class Student:
    __name=""
    def __init__(self, name):
        self.__name=name
    def getName(self):
        return self.__name

if __name__ =="__main__":
    student=Student("borphi")
    print(student.getName())
'''

#生成随机数字
'''
import random
def compareNum(num1, num2):
    if(num1 > num2):
        print("num1 is big")
        return 1
    elif(num1 == num2):
        print("num1 = num2")
        return 0
    else:
        print("num2 is big")
        return -1
num1 = random.randrange(1,9)
num2 = random.randrange(1,9)
print("num1 = ",num1)
print("num2 = ",num2)
print(compareNum(num1, num2))
'''

#规范倒入方式
'''
import sys
print(sys.path)
print(sys.argv)
'''

#不规范倒入方式
'''
from sys import path
from sys import argv
print(path)
print("\n")
print(argv)
print("\n")
'''

'''
class A:
    def funX(self):
        print("funY()")

    def funY(self):
        print("funY()")

if __name__ == "__main__":
    a = A()
    a.funX()
    a.funY()
'''

'''
def compareNum(num1, num2):
    if(num1 > num2):
        return str(num1)+"> "+str(num2)
    elif (num1 < num2):
        return str(num1)+"< "+str(num2)
    elif (num1 == num2):
        return str(num1)+"= "+str(num2)
    else:
        return ""

num1 = 2
num2 = 1
print(compareNum(num1, num2))

num1 = 2
num2 = 2
print(compareNum(num1, num2))

num1 = 1
num2 = 2
print(compareNum(num1, num2))
'''

#全局变量
'''
_a = 1
_b = 2
def add():
    global _a
    _a = 3
    return "_a + _b =",_a + _b
def sub():
    global _b
    _b = 4
    return "_a - _b =",_a - _b
print(add())
print(sub())
'''

#局部变量
'''
_a = 1
_b = 2
def add():
    _a = 3
    return "_a + _b =",_a + _b
def sub():
    _b = 4
    return "_a - _b =",_a - _b
print(add())
print(sub())
'''

#常量：定义一个常量模块const
#不明白
'''
class _const:
    class ConstError(TypeError):pass
    def __setattr__(self,name,value):
        if self.__dict__.has_key(name):
            raise self.ConstError,"Can't rebind const(%s)"%name
            self.__dict__[name]=value
import sys
sys.modules[__name__]=_const()
'''

'''
i = 1
print(type(i))
'''

#三引号的使用
'''
str1 = 'he say "hello world!"'
print(str1)
'''

#三引号制作doc文档:有问题，跟书上的输出结果不一样
'''
class Hello:   
    def printHello():
        ''' 'print hello world' '''
        print("hello world!")
print(Hello.__doc__)
print(Hello.printHello.__doc__)
'''

#if elif else语句
'''
score = float (input("score:"))
if 90 <= score <= 100:
    print("A")
elif 80 <= score < 90:
    print("B")
elif 60 <= score < 80:
    print("C")
else:
    print("D")
'''