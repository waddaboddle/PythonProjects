from colorgram import extract
from turtle import Turtle, Screen, colormode
from random import randint, choice

# colors = extract('image.jpg', 26)
#
# color_list = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     color_list.append(rgb)

color_list = [(199, 175, 117), (124, 36, 24), (168, 106, 57), (186, 158, 53), (6, 57, 83), (109, 67, 85),
              (113, 161, 175),
              (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79),
              (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177),
              (176, 198, 203), (150, 115, 120)]

# 10x10
# dot size = 20
# spaced = 50

timmy = Turtle()
colormode(255)
timmy.pensize(20)

screen = Screen()
screen.setworldcoordinates(-1, -1, 500, 500)


def random_color():
    color = choice(color_list)
    return color


def move_sideways():
    timmy.hideturtle()
    timmy.speed("fastest")
    timmy.penup()
    timmy.forward(50)


def move_up():
    timmy.hideturtle()
    timmy.speed("fastest")
    timmy.goto(0, timmy.ycor() + 50)


for _ in range(110):
    if timmy.xcor() < 500:
        timmy.dot(20, random_color())
        move_sideways()
    else:
        move_up()

screen = Screen()
screen.exitonclick()
