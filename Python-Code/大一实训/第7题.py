import turtle

turtle.setup(500,500,100,200)
turtle.pencolor('red')
turtle.pensize(2)
turtle.penup()
turtle.goto(0,50)
turtle.pendown()
turtle.left(90)
turtle.circle(100,180)
turtle.circle(200,60)
turtle.goto(0,-180)
turtle.penup()
turtle.goto(0,50)
turtle.left(120)
turtle.pendown()
turtle.circle(-100,180)
turtle.circle(-200,60)
turtle.goto(0,-180)
turtle.done()