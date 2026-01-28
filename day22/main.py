from turtle import Turtle, Screen
import time

from day22.ball import Ball
from day22.paddle import Paddle
from day22.score import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=800)
screen.title("Pop")
screen.tracer(0)

l_paddle = Paddle(-350,0)
r_paddle = Paddle(350,0)
ball = Ball()
score = Score()

screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")


screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True

while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    # Detect collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Collision with Paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()


screen.exitonclick()