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
    color(167,169,172)
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
    color(66, 125, 244)
    left(182)
    begin_fill()
    curve(90,((100*scale)/4))
    forward(2*(100*scale))
    curve(92,((00*scale)/2.555))
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
    color(10,31,91)
    forward(scale*50)
    left(92)
    forward(scale*900)
    left(90)
    forward(scale*49.96954)
    end_fill()
    
#Cloud
def clouds():
    setheading(90)
    penup()
    pendown()
    color("blue")
    begin_fill()
    for i in range(180):
      forward(0.2)
      left(1)
    left(180)
    for i in range(180):
      forward(0.2)
      left(1)
    left(180)
    for i in range(180):
      forward(0.2)
      left(1)
    left(180)
    for i in range(180):
      forward(0.2)
      left(1)
    left(270)
    for i in range(180):
      forward(0.2)
      left(1)
    left(270)
    for i in range(180):
      forward(0.2)
      left(1)
    right(180)
    for i in range(180):
      forward(0.2)
      left(1)
    right(180)
    for i in range(180):
      forward(0.2)
      left(1)
    right(180)
    for i in range(180):
      forward(0.2)
      left(1)
    left(270)
    for i in range(180):
      forward(0.2)
      left(1)
    forward(0.5)
    end_fill()
clouds()

#Street



#Sun


def sunface():
    begin_fill() 
    color("yellow")
    penup()
    goto(400,250)
    pendown()
    circle(70)
    end_fill()
    penup()
    
    
    
def lefteye():
    begin_fill()
    color("white")
    goto(370,330)
    pendown()
    circle(10)
    penup()
    begin_fill()
    color("black")
    goto(370,330)
    circle(5)
    end_fill()
    end_fill()
    penup() 
def righteye():
    begin_fill()
    color("white")
    goto(430,330)
    pendown()
    circle(10)
    begin_fill()
    color("black")
    goto(430,330)
    circle(5)
    end_fill()
    end_fill()
    penup()
    
def mouth():
    goto(440,310)
    pendown()
    seth(235)
    for i in range(90):
       right(1)
       forward(1)


#Tree

def buildleaf():
   for i in range(10):
       begin_fill()
       color ("green")
       circle(30)
       right(45) 
       end_fill()
def buildwood():
       goto(10,-52) 
       begin_fill()
       color ("brown")
       forward(35)
       right(90)
       forward(32)
       right(90)
       forward(48)
       right(90)
       forward(10)
       end_fill()
       
buildleaf()
buildwood()


def buildleaf():
    for i in range(10):
        begin_fill()
        color (0,1,0)
        circle(30)
        right(45) 
        end_fill()
def buildwood():
    setheading(-90)
    begin_fill()
    color ("brown")
    forward(180)
    right(90)
    forward(20)
    right(90)
    forward(180)
    right(90)
    forward(15)
    right(90)
    forward(20)
    right(90)
    forward(10)
    end_fill()
penup()
goto(randint(-750, 750),-350)
pendown()
buildwood()
buildleaf()
#drawBus(150,-100,.35)
update()