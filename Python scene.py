from turtle import*
from random import*

colormode(255)
speed(0)
tracer(0)
ht()
penup()

def curve(angle, size):
    for i in range(0,angle,1):
        forward(size/angle)
        left(1)

def drawBus(x,y,scale):
    #bus wheels
    #wheel 1
    goto(x-(scale*160),y+(scale*12))
    pd()
    seth(90)
    begin_fill()
    circle(scale*50)
    end_fill()
    #wheel 2
    goto(x-(scale*860),y+(scale*12))
    pd()
    seth(90)
    begin_fill()
    circle(scale*50)
    end_fill()

    #bus body
    goto(x,y)
    seth(0)
    pendown()
    begin_fill()
    color(randint(100,200),169,172)
    forward(10*scale)
    curve(92,((100*scale)/2))
    forward(5*(100*scale))
    ws=pos()
    curve(90,((100*scale)/2))
    right(2)
    forward(10*(100*scale))
    curve(88,((100*scale)/2))
    forward((5*(100*scale)))
    curve(90,((100*scale)/2))
    end_fill()
    pu()

    #windshield
    goto(ws)
    pd()
    color(66, 125, randint(150,255))
    left(182)
    begin_fill()
    curve(90,((100*scale)/4))
    forward(2*(100*scale))
    curve(92,((100*scale)/2.555))
    end_fill()
    pu()

    #doors
    goto(x+((10*scale)-(scale*30)),y+(scale*25))
    pd()
    color(0,0,0)
    begin_fill()
    seth(90)
    forward((30*scale)*16)
    left(90)
    forward((30*scale)*2)
    left(90)
    forward((30*scale)*16)
    left(90)
    doorl=pos()
    end_fill()
    pu()
    goto(doorl)
    seth(180)
    forward(scale*10)
    pd()
    color(0,0,0)
    begin_fill()
    seth(90)
    forward((30*scale)*16)
    left(90)
    forward((30*scale)*2)
    win=pos()
    left(90)
    forward((30*scale)*16)
    left(90)
    end_fill()
    pu()

    #window #1
    goto(win)
    seth(180)
    forward(70*scale)
    color(66, 150, 255)
    pd()
    begin_fill()
    forward((scale*50)*5)
    win=pos()
    curve(90,(scale*50))
    forward((50*scale)*3)
    curve(90,(scale*50))
    forward((scale*50)*5)
    curve(90,(scale*50))
    forward((50*scale)*3)
    curve(90,(scale*50))
    end_fill()
    pu()

    #window #2
    goto(win)
    seth(180)
    forward(150*scale)
    color(66, 150, 255)
    pd()
    begin_fill()
    forward((scale*50)*5)
    win=pos()
    curve(90,(scale*50))
    forward((50*scale)*3)
    curve(90,(scale*50))
    s=pos()
    forward((scale*50)*5)
    curve(90,(scale*50))
    forward((50*scale)*3)
    curve(90,(scale*50))
    end_fill()
    pu()

    #stripe
    goto(s)
    seth(180)
    forward(scale*180)
    left(88)
    forward(scale*50)
    pd()
    begin_fill()
    color(randint(0,255),randint(0,255),randint(0,255))
    forward(scale*50)
    left(92)
    forward(scale*900)
    left(90)
    forward(scale*49.96954)
    end_fill()

drawBus(0,0,.5)