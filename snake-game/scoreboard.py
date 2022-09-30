from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.fillcolor("white")
        self.goto(x=0, y=280)
        self.hideturtle()
        self.update_score()

    def game_over(self):
        self.clear()
        self.goto(x=0, y=0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
