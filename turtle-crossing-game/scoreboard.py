from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(x=0, y=280)
        self.fillcolor("black")
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-250, 270)
        self.write(f"Level: {self.level}", align="center", font=("Courier", 12, "normal"))

    def level_up(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=("Courier", 12, "normal"))



