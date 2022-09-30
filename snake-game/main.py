from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
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
scoreboard = ScoreBoard()

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
        scoreboard.increase_score()
        snake.extend()
    # Detect collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
    # Detect collision with its own tail
    for square in snake.squares[1:]:
        if snake.head.distance(square) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
