import turtle
def drawSquare(forward):
    for i in range (15):
        turtle.seth(90)
        turtle.fd(forward)
        turtle.seth(0)
        turtle.fd(forward)
        forward = forward - 10

        turtle.seth(-90)
        turtle.fd(forward)
        turtle.seth(180)
        turtle.fd(forward)
        forward = forward - 10
turtle.setup(1000, 700, None, None)
turtle.penup()
turtle.fd(-250)
turtle.seth(-90)
turtle.fd(100)
turtle.pendown()
turtle.pensize(1)
turtle.pencolor("red")
drawSquare(300)
turtle.done()