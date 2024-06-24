import turtle
from turtle import Turtle, Screen, colormode
from random import choice, randint

timmy = Turtle()
turtle.colormode(255)

turns = [-90, 0, 90, 180]

timmy.pensize(10)
timmy.speed(8)


def random_color():
    R = randint(0, 255)
    G = randint(0, 255)
    B = randint(0, 255)
    color = (R, G, B)
    return color


for _ in range(200):
    timmy.pencolor(random_color())
    timmy.forward(25)
    timmy.setheading(choice(turns))

screen = Screen()
screen.exitonclick()
