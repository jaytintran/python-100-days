from turtle import Screen
import turtle as t
import random
# import heroes

tom_the_turtle = t.Turtle()
t.colormode(255)
tom_the_turtle.shape("turtle")
tom_the_turtle.color("red")


# Challenge 1
# angle = 360 / num_slides
# for i in range(num_slides)

colors = ["red", "blue", "green", "orange"]


# def draw_shape(num_slides):
#     angle = 360 / num_slides
#     for i in range(num_slides):
#         tom_the_turtle.forward(100)
#         tom_the_turtle.right(angle)
#
#
# for shape_side_from_n in range(3, 11):
#     tom_the_turtle.color(random.choice(colors))
#     draw_shape(shape_side_from_n)

# Challenge 2
# random_direction = []

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# random_direction = [0, 90, 180, 270]
tom_the_turtle.speed("fastest")
# tom_the_turtle.pensize(15)
#
# for i in range(200):
#     tom_the_turtle.color(random_color())
#     tom_the_turtle.setheading(random.choice(random_direction))
#     tom_the_turtle.forward(30)
#

# Challenge 3

current_heading = tom_the_turtle.heading()


def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tom_the_turtle.color(random_color())
        tom_the_turtle.circle(100)
        tom_the_turtle.setheading(tom_the_turtle.heading() + size_of_gap)

draw_spirograph(5)

my_screen = Screen()
my_screen.exitonclick()
