import turtle

turtle.Screen().bgcolor("orange");
turtle.Screen().setup(500,500)
t = turtle.Turtle()

n_sides =6
side_len = 100
angle = 360/6

for i in range(n_sides):
    t.forward(side_len)
    t.left(angle)

turtle.done()