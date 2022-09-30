from turtle import Screen
from pong import Pong
from player import Player
from scoreboard import ScoreBoard
import time

GAME_SPEED = 0.1

# Init the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong Game")
# Turn off the animation
screen.tracer(0)

# Init the ball
ball = Pong()
scoreboard = ScoreBoard()

# Init players
player1 = Player((-350, 0))
player2 = Player((350, 0))

# Listen for keystrokes
screen.listen()
screen.onkey(player1.up, "w")
screen.onkey(player1.down, "s")
screen.onkey(player2.up, "Up")
screen.onkey(player2.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(GAME_SPEED)
    screen.update()
    ball.move()

    # Detect if ball hits the damn wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # It bounces
        ball.bounce_y()

    # Detect if ball hits the player
    if ball.distance(player1) < 50 or ball.distance(player2) < 50:
        if ball.xcor() > 320:
            ball.bounce_x()
            GAME_SPEED = GAME_SPEED / 2
        if ball.xcor() < -320:
            ball.bounce_x()
            GAME_SPEED = GAME_SPEED / 2

    # Detect if ball goes off the screen
    if ball.xcor() > 380:
        # Delay 1s
        time.sleep(0.5)
        # Restart the ball
        ball.restart()
        # Player 1 gets 1 point
        scoreboard.l_point()
        # Reset time speed
        GAME_SPEED = 0.1

    if ball.xcor() < -380:
        # Delay 1s
        time.sleep(0.5)
        # Restart the ball
        ball.restart()
        # Player 2 gets 1 point
        scoreboard.r_point()
        # Reset time speed
        GAME_SPEED = 0.1

screen.exitonclick()
