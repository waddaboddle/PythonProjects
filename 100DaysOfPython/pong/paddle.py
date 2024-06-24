from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.new_y = 0
        self.shape("square")
        self.penup()
        self.color("White")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def up(self):
        self.new_y = self.ycor() + 20
        self.goto(self.xcor(), self.new_y)

    def down(self):
        self.new_y = self.ycor() - 20
        self.goto(self.xcor(), self.new_y)
