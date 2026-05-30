import turtle

drawer = turtle.Turtle()
canvas = turtle.Screen()

shadeList = ["cyan", "red", "green", "blue", "magenta", "white"]

canvas.bgcolor("black")

drawer.speed(0)
drawer.hideturtle()

while True:
    for step in range(180):
        drawer.pencolor(shadeList[step % len(shadeList)])
        drawer.width(step / 120 + 1)
        drawer.forward(step)
        drawer.left(58)

    drawer.left(240)

    for step in range(180, 0, -1):
        drawer.pencolor("black")
        drawer.width(step / 120 + 6)
        drawer.forward(step)
        drawer.right(58)