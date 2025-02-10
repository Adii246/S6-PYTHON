import turtle
x=turtle.Turtle()
x.shape("turtle")
x.fillcolor("yellow")
x.penup()
x.goto(0,0)
x.pendown()
x.speed(20)
for i in range(10):
    x.circle(100)
    x.right(20)
    x.circle(100)
    x.right(20)
turtle.done()
