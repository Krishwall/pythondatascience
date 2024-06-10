from turtle import *
import random
t=Turtle()
r=2
s=Screen()
s.setup(600,700,startx=None,starty=None)
s.screensize(1000,2000)
speed('fastest')
while True:
    r*=2
    x=random.randint(2,300)
    y=random.randint(2,300)
    penup()
    goto(x,y)
    pendown()
    pencolor('red')
    for i in range(50):
        fd(i*2+5)
        rt(60)
    
    

mainloop()    