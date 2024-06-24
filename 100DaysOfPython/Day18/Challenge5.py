import turtle
from turtle import Turtle, Screen
from random import randint

timmy = Turtle()
turtle.colormode(255)

timmy.speed("fastest")


def random_color():
    R = randint(0, 255)
    G = randint(0, 255)
    B = randint(0, 255)
    color = (R, G, B)
    return color


def draw_spiral(gap_size):
    for _ in range(int(360 / gap_size)):
        timmy.color(random_color())
        timmy.setheading(timmy.heading() + gap_size)
        timmy.circle(100)


draw_spiral(1)

screen = Screen()
screen.exitonclick()
