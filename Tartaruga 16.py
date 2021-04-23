import turtle
import random

a = turtle.Screen()

t = turtle.Turtle()
turtle.Screen().bgcolor("gray")
cores = ["cyan", "purple", "white", "blue"]

t.pen()
t.forward(90)
t.left(45)
t.pendown()

def ramo():
    for i in range(3):
        for i in range(3):
            t.forward(30)
            t.backward(30)
            t.right(45)
        t.left(90)
        t.backward(30)
        t.left(45)
    t.right(90)
    t.forward(90)

for i in range(8):
    ramo()
    t.left(45)

a.exitonclick()

t.color(random.choice(cores))
