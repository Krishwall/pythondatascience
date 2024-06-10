from turtle import *
import time
import math

n=int(input("enter the no. of sides"))

s=getscreen()
t=Turtle()

t.shapesize(5,5,5)
t.color("red","lime")
t.begin_fill()


for i in range(1,n+1):
  t.fd(100)
  t.lt(360/n)
  time.sleep(0.0005)
  t.end_fill()
t.home()
t.rt(180/n)
t.color("black","grey")
t.begin_fill()

t.circle(50/math.sin(math.pi/n))
t.end_fill()

mainloop()


