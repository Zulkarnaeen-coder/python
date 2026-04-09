import turtle

turtle.Screen().bgcolor("green")
turtle.color("red")
turtle.Screen().setup(500,500)
t = turtle.Turtle()

for i in range(4):
    t.forward(90)
    t.left(90)

turtle.done()