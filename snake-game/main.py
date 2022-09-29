from turtle import Screen
from snake import Snake
from food import Food
import time

# Init the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Init the snake
snake = Snake()
food = Food()

# Control the snake via listening to keystrokes
screen.listen()
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

# Run the game
game_is_on = True
while game_is_on:
    # Update the tracer for smoother animation
    screen.update()
    # Slow down the animation
    time.sleep(0.125)
    # Move the snake
    snake.move()
    # Detect if snake meets the food dot
    if snake.head.distance(food) < 15:
        # Spawning the food randomly other place on the map
        food.spawning()

screen.exitonclick()
