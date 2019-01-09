import turtle
import random

turtle.colormode(255)
turtle.speed(0)
turtle.tracer(0)
turtle.ht()
turtle.penup()

def curve(angle, size):
    turtle.pd()
    for i in range(0,angle,1):
        turtle.forward(size/angle)
        turtle.left(1)
    turtle.pu()

def drawBus(x,y,scale):
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(167,169,172)
    turtle.forward(10*scale)
    curve(91,(scale/2))
    turtle.forward(5*scale)
    pos=
    curve(90,(scale/2))
    turtle.forward(10*scale)
    curve(88,(scale/2))
    turtle.forward(5*scale)
    curve(90,(scale/2))
    turtle.end_fill()
    
drawBus(-70,0,50)