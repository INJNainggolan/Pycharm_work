
from turtle import *
setup(650, 350, None, None)
penup()
fd(-250)
pendown()
pensize(10)
pencolor("purple")
seth(-40)
for i in range (4):
    circle(40, 80)
    circle(-40, 80)
circle(40, 80/2)
fd(40)
circle(16, 180)
fd(40 * 2/3)