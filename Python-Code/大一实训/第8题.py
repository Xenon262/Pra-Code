from turtle import *

setup(400,400)
penup()
goto(0,-50)
pendown()
pencolor("light green")
fillcolor("light green")
begin_fill()
circle(100,360)
for i in range(1):
    right(90)
    forward(100)
end_fill()
hideturtle()
done()