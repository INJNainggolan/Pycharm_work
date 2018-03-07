'''
import turtle
def drawHeart():
    turtle.seth(150)
    turtle.fd(140)
    turtle.seth(125)
    turtle.fd(130)
    turtle.seth(105)
    turtle.fd(100)
    turtle.seth(75)
    turtle.fd(100)
    turtle.seth(35)
    turtle.fd(110)
    turtle.seth(-20)
    turtle.fd(110)
    turtle.seth(-40)
    turtle.fd(80)
    turtle.seth(-75)
    turtle.fd(50)
turtle.setup(1000, 600, None, None)
turtle.penup()
turtle.seth(-90)
turtle.fd(200)
turtle.pendown()
turtle.pensize(1)
turtle.pencolor("red")
drawHeart()
turtle.done()
'''


'''
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-8, 8, 1024)
y1 = 0.618*np.abs(x) - 0.8*np.aqrt(64 - x ** 2)
y1 = 0.618*np.abs(x) + 0.8*np.aqrt(64 - x ** 2)
plt.plot(x, y1, color = "r")
plt.plot(x, y2, color = "r")
plt.show()
'''

#heart

from turtle import *
from time import sleep

def go_to(x, y):
   up()
   goto(x, y)
   down()


def big_Circle(size):  #函数用于绘制心的大圆
#   speed(1)
   for i in range(150):
       forward(size)
       right(0.3)

def small_Circle(size):  #函数用于绘制心的小圆
#   speed(1)
   for i in range(210):
       forward(size)
       right(0.786)

def line(size):
#   speed(1)
   forward(51*size)

def heart( x, y, size):
   go_to(x, y)
   left(150)
   begin_fill()
   line(size)
   big_Circle(size)
   small_Circle(size)
   left(120)
   small_Circle(size)
   big_Circle(size)
   line(size)
   end_fill()

def arrow():
   pensize(10)
   setheading(0)
   go_to(-400, 0)
   left(15)
   forward(150)
   go_to(339, 178)
   forward(150)

def arrowHead():
   pensize(1)
   speed(150)
   color('red', 'red')
   begin_fill()
   left(120)
   forward(20)
   right(150)
   forward(35)
   right(120)
   forward(35)
   right(150)
   forward(20)
   end_fill()


def main():
   pensize(2)
   color('pink', 'red')
   #getscreen().tracer(30, 0) #取消注释后，快速显示图案
   heart(200, 0, 1)          #画出第一颗心，前面两个参数控制心的位置，函数最后一个参数可控制心的大小
   setheading(0)             #使画笔的方向朝向x轴正方向
   heart(-80, -100, 1.4)     #画出第二颗心
   arrow()                   #画出穿过两颗心的直线
   arrowHead()               #画出箭的箭头
   go_to(40, -100)
   write("宝宝乖", move=True, align="left", font=("宋体", 30, "normal"))
   done()

main()