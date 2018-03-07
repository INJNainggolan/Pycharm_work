#equilateral_triangle

import turtle

def draw_equilateral_triangle(rad):
    turtle.seth(-60)
    turtle.fd(rad)
    turtle.seth(-180)
    turtle.fd(rad)
    turtle.seth(60)
    turtle.fd(rad)

def main():
    turtle.setup(1300,800,0,0)
    pythonsize = 10
    turtle.pensize(pythonsize)
    turtle.pencolor("blue")
    draw_equilateral_triangle(80)

main()