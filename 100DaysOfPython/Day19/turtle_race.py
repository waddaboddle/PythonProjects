import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
racers = []


def set_turtle_start(racer, y_loc):
    racer.penup()
    racer.goto(-240, y_loc)


for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    set_turtle_start(new_turtle, 30 * i - 90)
    racers.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for racer in racers:
        if racer.xcor() > 230:
            is_race_on = False
            winning_color = racer.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_dist = random.randint(0, 10)
        racer.forward(rand_dist)


screen.exitonclick()
