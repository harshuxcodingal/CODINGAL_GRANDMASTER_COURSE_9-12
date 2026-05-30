import turtle

pen = turtle.Turtle()
screen = turtle.Screen()

screen.bgcolor("lightyellow")

for i in range(3):
    pen.forward(100)
    pen.left(120)

pen.penup()
pen.goto(-150, 0)
pen.pendown()

for i in range(4):
    pen.forward(100)
    pen.left(90)

pen.penup()
pen.goto(150, 0)
pen.pendown()

for i in range(6):
    pen.forward(60)
    pen.left(60)

turtle.done()