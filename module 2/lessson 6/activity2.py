import turtle

turtle.Screen().bgcolor("Blue")
turtle.color("red")
turtle.pensize(10)
turtle.Screen().setup(500,500)
t = turtle.Turtle()

t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)

t.penup()
t.right(150)
t.forward(50)

t.pendown()
t.right(90)
t.forward(100)
t.right(120)
t.forward(100)
t.right(120)
t.forward(100)

turtle.done()