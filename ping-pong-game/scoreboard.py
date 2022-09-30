from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(x=0, y=280)
        self.fillcolor("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 250)
        self.write(self.l_score, align="center", font=("Courier", 20, "normal"))
        self.goto(100, 250)
        self.write(self.r_score, align="center", font=("Courier", 20, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()



