#switch语句：Python并没有switch语句，但是可以通过字典实现switch语句功能
'''
from __future__ import division
x = 1
y = 2
operator = "/"
result = {
    "+": x + y,
    "-": x - y,
    "*": x * y,
    "/": x / y
}
print(result.get(operator))
'''

#使用switch类实现switch功能
'''
class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        yield self.match
        raise StopIteration

    def match(self, *args):
        if self.fall or not args:
            return True
        elif self.value in args:
            self.fall = True
            return True
        else:
            return False

operator = "+"
x = 1
y = 2
for case in switch(operator):
    if case('+'):
        print(x + y)
        break
    if case('-'):
        print(x - y)
        break
    if case('*'):
        print(x * y)
        break
    if case('/'):
        print(x / y)
        break
#    if case():
#       print ""
'''

#while循环
'''
numbers = input("输入几个数字，用逗号分隔：").split(",")
print(numbers)
x = 0
while x<len(numbers):
    print(numbers[x])
    x += 1
'''

#带else子句的while循环
'''
x = float(input("输入x的值："))
i = 0
while(x != 0):
    if(x > 0):
        x -= 1
    else:
        x += 1
    i = i+1
    print("第%d次循环：%d"%(i,x))
else:
    print("x等于0：",x)
'''

#for in 语句
'''
for x in range(-1, 2):
    if x > 0:
        print("正数：",x)
    elif x == 0:
        print("零：",x)
    else:
        print("负数：",x)
else:
    print("循环结束")
'''

#从0到99查找用户输入的值
'''
x = int(input("输入x的值:"))
#y = 0
i = 0
for y in range(0, 100):
    if x == y:
        print("找到数字：",x)
        break
    else:
        i += 1
        print("没有找到,第%d次查找"% (i))
'''

#continue语句
'''
x = 0
for i in [1,2,3,4,5]:
    if x == i:
        continue
    print("///",x)
    x += i
    print(x)
print("x的值为：",x)
'''

'''
s="abcd1234"
print(s.find("cd"))
'''

'''
def compareNum(num1,num2):
    if(num1 > num2):
        return str(num1)+">"+str(num2)
    elif(num1 < num2):
        return str(num1)+"<"+str(num2)
    elif(num1 == num2):
        return str(num1)+"="+str(num2)
    else:
        return ""

num1 = 2
num2 = 1
print(compareNum(num1,num2));
num1 = 2
num2 = 2
print(compareNum(num1,num2))
num1 = 1
num2 = 2
print(compareNum(num1,num2))
'''

'''
def fun():
    local = 1
    print(local)
fun()
print("ERROR")
'''
'''
#在文件的开头定义全局变量
_a = 1
_b = 2
def add():
    #引用全局变量_a
    global _a
    _a = 3
    return "_a + _b =", _a + _b
def sub():
    #引用全局变量_b
    global _b
    _b = 4
    return "_a - _b =", _a - _b
print(add())
print(sub())

#在文件的开头定义全局变量(错误示范)
_a = 1
_b = 2
def add():
    _a = 3
    return "_a + _b =", _a + _b
def sub():
    _b = 4
    return "_a - _b =", _a - _b
print(add())
print(sub())
'''

'''
#调用全局变量
import gl
def fun():
    print(gl._a)
    print(gl._b)
fun()
'''

'''
#常量
class _const:
    class ConstError(TypeError):pass
    def __setattr__(self,name,value):
        if self.__dict__.has_key(name):
            raise self.ConstError,"Can't rebind const(%s)"%name
            self.__dict__[name] = value
import sys
sys.modules [__name__] = _const()
'''

'''
#整型
i = 1
print(type(i))
#长整型
l = 999999999999999999999999999999999999999999999999999999999999990
print(type(l))
#浮点型
f = 1.2
print(type(f))
#布尔型
b = True
print(type(b))
#复数类型
c = 7 + 8j
print(type(c))
'''

'''
有问题
'''

#三引号制作的doc文档
'''
class Hello:
    ''''''hello class''''''
    print("RRRRRR")
    def printHello():
        ''''''print hello world''''''
        print("!!!!!!!")
        print("hello world!")
print(Hello.__doc__)
print("QQQQQQQ")
print(Hello.printHello.__doc__)
'''