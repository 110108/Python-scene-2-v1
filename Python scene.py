import turtle
import random

turtle.colormode(255)
turtle.speed(0)
turtle.tracer(0)
turtle.ht()
turtle.penup()

def curve(angle, size):
    for i in range(0,angle,1):
        turtle.forward(size/angle)
        turtle.left(1)

def drawBus(x,y,scale):
    #bus wheels
    #wheel 1
    turtle.goto(x-(scale*160),y+(scale*12))
    turtle.pd()
    turtle.seth(90)
    turtle.begin_fill()
    turtle.circle(scale*50)
    turtle.end_fill()
    #wheel 2
    turtle.goto(x-(scale*860),y+(scale*12))
    turtle.pd()
    turtle.seth(90)
    turtle.begin_fill()
    turtle.circle(scale*50)
    turtle.end_fill()
    
    #bus body
    turtle.goto(x,y)
    turtle.seth(0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(167,169,172)
    turtle.forward(10*scale)
    curve(92,((100*scale)/2))
    turtle.forward(5*(100*scale))
    ws=turtle.pos()
    curve(90,((100*scale)/2))
    turtle.right(2)
    turtle.forward(10*(100*scale))
    curve(88,((100*scale)/2))
    turtle.forward((5*(100*scale)))
    curve(90,((100*scale)/2))
    turtle.end_fill()
    turtle.pu()
    
    #windshield
    turtle.goto(ws)
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
    turtle.goto(x+((10*scale)-(scale*30)),y+(scale*25))
    turtle.pd()
    turtle.color(0,0,0)
    turtle.begin_fill()
    turtle.seth(90)
    turtle.forward((30*scale)*16)
    turtle.left(90)
    turtle.forward((30*scale)*2)
    turtle.left(90)
    turtle.forward((30*scale)*16)
    turtle.left(90)
    doorl=turtle.pos()
    turtle.end_fill()
    turtle.pu()
    turtle.goto(doorl)
    turtle.seth(180)
    turtle.forward(scale*10)
    turtle.pd()
    turtle.color(0,0,0)
    turtle.begin_fill()
    turtle.seth(90)
    turtle.forward((30*scale)*16)
    turtle.left(90)
    turtle.forward((30*scale)*2)
    win=turtle.pos()
    turtle.left(90)
    turtle.forward((30*scale)*16)
    turtle.left(90)
    turtle.end_fill()
    turtle.pu()
    
    #window #1
    turtle.goto(win)
    turtle.seth(180)
    turtle.forward(70*scale)
    turtle.color(66, 150, 255)
    turtle.pd()
    turtle.begin_fill()
    turtle.forward((scale*50)*5)
    win=turtle.pos()
    curve(90,(scale*50))
    turtle.forward((50*scale)*3)
    curve(90,(scale*50))
    turtle.forward((scale*50)*5)
    curve(90,(scale*50))
    turtle.forward((50*scale)*3)
    curve(90,(scale*50))
    turtle.end_fill()
    turtle.pu()
    
    #window #2
    turtle.goto(win)
    turtle.seth(180)
    turtle.forward(150*scale)
    turtle.color(66, 150, 255)
    turtle.pd()
    turtle.begin_fill()
    turtle.forward((scale*50)*5)
    win=turtle.pos()
    curve(90,(scale*50))
    turtle.forward((50*scale)*3)
    curve(90,(scale*50))
    s=turtle.pos()
    turtle.forward((scale*50)*5)
    curve(90,(scale*50))
    turtle.forward((50*scale)*3)
    curve(90,(scale*50))
    turtle.end_fill()
    turtle.pu()
    
    #stripe
    turtle.goto(s)
    turtle.seth(180)
    turtle.forward(scale*180)
    turtle.left(88)
    turtle.forward(scale*50)
    turtle.pd()
    turtle.begin_fill()
    turtle.color(10,31,91)
    turtle.forward(scale*50)
    turtle.left(92)
    turtle.forward(scale*900)
    turtle.left(90)
    turtle.forward(scale*49.96954)
    turtle.end_fill()
    
drawBus(100,10,.5)
turtle.update()