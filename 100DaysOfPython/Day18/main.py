import turtle
from turtle import Turtle, Screen, colormode
from random import randint

timmy = Turtle()
timmy.shape("turtle")
turtle.colormode(255)


def polygon(sides):
    timmy.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
    for _ in range(0, sides):
        timmy.forward(100)
        timmy.right(360 / sides)


for sides in range(3, 11):
    polygon(sides)

screen = Screen()
screen.exitonclick()
