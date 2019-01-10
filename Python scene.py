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
    #bus body
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(167,169,172)
    turtle.forward(10*scale)
    curve(92,((100*scale)/2))
    turtle.forward(5*(100*scale))
    pos=turtle.pos()
    curve(90,((100*scale)/2))
    turtle.right(2)
    turtle.forward(10*(100*scale))
    curve(88,((100*scale)/2))
    turtle.forward((5*(100*scale)))
    curve(90,((100*scale)/2))
    turtle.end_fill()
    turtle.pu()
    
    #windshield
    turtle.goto(pos)
    turtle.pd()
    turtle.color(66, 125, 244)
    turtle.left(182)
    turtle.begin_fill()
    curve(90,((100*scale)/4))
    turtle.forward(2*(100*scale))
    curve(92,((100*scale)/2.555))
    turtle.end_fill()
    turtle.pu()
    
    #doors
    turtle.goto(x+(
    
drawBus(-200,-100,1)
turtle.update()