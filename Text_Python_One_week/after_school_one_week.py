#1ST
'''
str1 = input("请输入一个人的名字：")
str2 = input("请输入一个国家名字：")
print("世界这么大，{}想去{}看看".format(str1,str2))
'''

#2nd
'''
n = input("请输入整数：")
sum = 0
for i in range(int(n)):
    sum += i + 1
print("1到n的求和结果为：",sum)
'''

#3rd
'''
for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={:2}  ".format(j,i,j*i),end='')
    print('')
'''

#4th
'''
sum , tmp = 0 , 1
for i in range(1,11):
    tmp *= i
    sum += tmp
print("运算结果是：{}".format(sum))
'''

#5th
'''
n = 1
for i in range(5,0,-1):
    n = (n+1) << 1
print(n)
'''

#6th
'''
diet = ['西红柿','花椰菜','黄瓜','牛排','虾仁']
for x in range(0,5):
    for y in range(0,5):
        if not(x==y):
            print("{}{}".format(diet[x],diet[y]))
'''

#7th
'''
from turtle import *
fillcolor("red")
begin_fill()
while True:
    forward(200)
    right(144)
    if abs(pos()) < 1:
        break
end_fill()
'''

#8th
'''
from turtle import *
color ('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
'''

#9th
'''
import turtle
import time
turtle.speed("fastest")
turtle.pensize(2)
for x in range(100):
    turtle.forward(2*x)
    turtle.left(90)
time.sleep(3)
'''

#10th

import turtle
import time
turtle.pensize(2)
turtle.bgcolor("black")
colors = ["red","yellow","purple","blue"]
turtle.tracer(False)
for x in range(400):
    turtle.forward(2*x)
    turtle.color(colors[x % 4])
    turtle.left(91)
turtle.tracer(True)
