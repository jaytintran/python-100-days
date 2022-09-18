import random
import turtle
import turtle as t
from turtle import Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter color: ")
colors = ["red", "blue", "green", "orange", "purple", "pink"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
top_three_winners = []
print(user_bet)

for turtle_index in range(0, 6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            top_three_winners.append(turtle)
            if len(top_three_winners) == 2:
                is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_step = random.randint(0, 10)
        turtle.forward(random_step)


# babby = t.Turtle()
# zacky = t.Turtle()
# pipo = t.Turtle()
#
# tim.color("green")
# babby.color = "blue"
# zacky.color = "red"
# pipo.color = "black"

screen.exitonclick()

