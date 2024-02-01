from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 14, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("max_score.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=True, align=ALIGNMENT, font=FONT)
        self.goto(x=0, y=270)

    def reset(self):
        """ Save max score in txt"""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("max_score.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        """ Add point to the score """
        self.score += 1
        self.goto(x=0, y=270)
        self.update_scoreboard()
