# 1. setup screen
# 2. scoreboard
# 3. ball movement
# 4. player movements
# 4a. computer will move up and down if no two player
import turtle
from turtle import Screen, Turtle
import time
from paddles import CreatePaddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game v2")
screen.tracer(0)

scoreboard = Scoreboard()

# player = Turtle()
# player.color('white')
# player.shape('square')
# player.shapesize(stretch_wid=5, stretch_len=1)
# player.penup()
# player.goto(350, 0)

# Create Two Paddles for Pong Game
right_paddle = CreatePaddle((350, 0))
left_paddle = CreatePaddle((-350, 0))
# create ball for game
ball = Ball()

screen.listen()
# Control the Right Paddle
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
# Control the Left Paddle
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detect Collision to Top/Bottom Walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Needs to Bounce
        ball.bounce_y()
    # Detect Collision with Paddles Hit Ball
    if ball.distance(right_paddle) < 50 and ball.xcor() > 330 \
            or ball.distance(left_paddle) < 50 and ball.xcor() < -330:
        # print(f"Paddle Hit")
        ball.bounce_x()
    # Detect when Right Paddle Misses Ball, Increase Point for Left Player
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()

    # Detect when Left Paddle Misses Ball, Increase Point for Right Player
    if ball.xcor() < -380:
        scoreboard.right_point()
        ball.reset_position()

screen.exitonclick()

# if __name__ == '__main__':
