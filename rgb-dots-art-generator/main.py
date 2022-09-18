import colorgram
from turtle import Turtle, Screen
import turtle as t
import random

colors = colorgram.extract('image.jpg', 30)
rgb_color = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_color.append(new_color)

print(rgb_color)

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
              (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
              (107, 127, 153), (176, 192, 208), (168, 99, 102)]


def random_color():
    set_of_color = random.choice(color_list)
    red = set_of_color[0]
    green = set_of_color[1]
    blue = set_of_color[2]
    color_dot = (red, green, blue)
    return color_dot


pencil = Turtle()
pencil.penup()
pencil.goto(-200, -200)
pencil.down()
pencil.pensize(20)
pencil.speed("fastest")
t.colormode(255)


def draw_line():
    for i in range(10):
        pencil.color(random_color())
        # pencil.color("blue")
        pencil.dot(20)
        pencil.penup()
        pencil.forward(50)
        pencil.pendown()
        pencil.dot(20)
        pencil.penup()


def new_line_max_x():
    pencil.setheading(90)
    pencil.forward(50)
    pencil.setheading(180)


def new_line_min_x():
    pencil.setheading(90)
    pencil.forward(50)
    pencil.setheading(360)


draw_line()
x = 10

for i in range(9):
    if x == 10:
        new_line_max_x()
        draw_line()
        x = 0
    elif x == 0:
        new_line_min_x()
        draw_line()
        x = 10


my_paper = Screen()
my_paper.screensize(1000, 500)
my_paper.exitonclick()



