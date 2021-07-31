import turtle

turtle = turtle.Turtle()
turtle.speed(10)

"""for i in range(12):
    for i in range(91):
        turtle.forward(100)
        turtle.right(91)
    turtle.left(30)
    turtle.forward(50)"""

"""count = 1
for i in range(10):
    count += 1
    for i in range(360):
        turtle.left(1)
        turtle.forward(count)"""


def build_car():
    for i in range(450):
        turtle.left(1)
        turtle.forward(1)

    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)

    for i in range(540):
        turtle.left(1)
        turtle.forward(1)

    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)

    for i in range(90):
        turtle.left(1)
        turtle.forward(1)

    turtle.forward(50)
    turtle.right(90)

    for i in range(90):
        turtle.left(1)
        turtle.forward(1)

    turtle.forward(100)

    for i in range(90):
        turtle.left(1)
        turtle.forward(1)

    turtle.right(90)
    turtle.forward(50)

    for i in range(90):
        turtle.left(1)
        turtle.forward(1)

    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)


build_car()