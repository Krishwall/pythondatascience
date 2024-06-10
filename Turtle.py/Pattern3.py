from turtle import *
s=Screen()
s.setup(1000,700)
s.screensize(2000,1500)
pencolor('red')
pensize(3)
y=20

for i in range(10,0,-1):
     if(i%2==0):
          fillcolor('orange')
          begin_fill()
          circle(i*20)
          end_fill()
     else:
            fillcolor('black')
            begin_fill()
            circle(i*20)
            end_fill()
     penup()
     goto(0,y)
     pendown()
     y+=20
mainloop()

       
      
 
