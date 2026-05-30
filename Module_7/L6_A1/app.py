import turtle

window = turtle.Screen()
window.setup(500, 400)
window.bgcolor("lightblue")
window.title("Shape Drawing")

pen = turtle.Turtle()

for side in range(4):
    pen.forward(120)
    pen.right(90)

turtle.done()