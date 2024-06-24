from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(open("data.txt").read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            open("data.txt", mode="w").write(str(self.high_score))
        self.score = 0
        self.update()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update()
