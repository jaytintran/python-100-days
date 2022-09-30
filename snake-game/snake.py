from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.squares = []
        self.initialize_snake()
        self.head = self.squares[0]

    def initialize_snake(self):
        # For every position, give it a white square
        for position in STARTING_POSITION:
            self.add_square(position)

    def add_square(self, position):
        new_square = Turtle(shape="square")
        new_square.penup()
        new_square.color("white")
        new_square.goto(position)
        self.squares.append(new_square)

    def extend(self):
        # Add new square
        self.add_square(self.squares[-1].position())

    def move(self):
        # Remake the snake move
        for square_num in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[square_num - 1].xcor()
            new_y = self.squares[square_num - 1].ycor()
            self.squares[square_num].goto(new_x, new_y)
        # Move the head of the snake
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        # If the head is pointing up, it can't go down
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # If the head is pointing down, it can't go up
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        # If the head is pointing right, it can't go left
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        # If the head is pointing left, it can't go right
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

