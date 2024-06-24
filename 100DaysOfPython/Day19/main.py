import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


# W = FWD
# S = BWD
# A = CCW
# D = CW

def move_fwd():
    tim.forward(10)


def move_bwd():
    tim.backward(10)


def move_ccw():
    tim.setheading(tim.heading() + 5)


def move_cw():
    tim.setheading(tim.heading() - 5)


def clear():
    screen.reset()


def control_turtle():
    turtle.onkeypress(key="w", fun=move_fwd)  # don't add the parenthesis
    turtle.onkeypress(key="s", fun=move_bwd)
    turtle.onkeypress(key="a", fun=move_ccw)
    turtle.onkeypress(key="d", fun=move_cw)
    turtle.onkeypress(key="c", fun=clear)
    turtle.onkeypress(key="u", fun=tim.penup)
    turtle.onkeypress(key="j", fun=tim.pendown)


screen.listen()
control_turtle()
screen.exitonclick()
