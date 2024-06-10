from turtle import *
bgcolor('black')
speed('fastest')
#colors=['red','white']

colors=['red','purple','blue','green','yellow','orange']

for x in range(360):
    pencolor(colors[x%6])
    width(x/100+1)
    forward(x)
    left(100)
'''for x in range(360):
    pencolor(colors[x%2])
    width(x*5/100+1)
    forward(x*4)
    left(90)'''

penup()   
goto(0,-25)
pendown()
fillcolor('black')
begin_fill()
circle(30)
end_fill()
mainloop()