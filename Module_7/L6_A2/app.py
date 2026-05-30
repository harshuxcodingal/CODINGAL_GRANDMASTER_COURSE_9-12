import turtle

screen = turtle.Screen()
screen.setup(600, 500)
screen.bgcolor("yellow")
screen.title("Star Design")

artist = turtle.Turtle()

artist.forward(120)
artist.left(120)
artist.forward(120)
artist.left(120)
artist.forward(120)

artist.penup()
artist.left(30)
artist.forward(60)

artist.pendown()
artist.left(90)
artist.forward(120)
artist.left(120)
artist.forward(120)
artist.left(120)
artist.forward(120)

turtle.done()