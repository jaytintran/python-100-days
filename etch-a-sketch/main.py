from turtle import Turtle, Screen

pencil = Turtle()
screen = Screen()

pencil.pensize(5)
pencil.color("blue")


def move_forward():
    pencil.forward(10)


def move_backward():
    pencil.backward(10)


def turn_left():
    pencil.left(10)


def turn_right():
    new_heading = pencil.heading() - 10
    pencil.setheading(new_heading)


def clear_screen():
    pencil.clear()
    pencil.penup()
    pencil.home()
    pencil.pendown()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_screen, "c")
screen.exitonclick()