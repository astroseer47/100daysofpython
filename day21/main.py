from turtle import Screen
import time

from score_board import ScoreBoard
from food import Food
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

is_game_on = True

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        score_board.increase_score()
        snake.extend()
        snake.extend()
        snake.extend()
        snake.extend()
        snake.extend()
        snake.extend()
        snake.extend()
        food.refresh()


    x_cor = snake.head.xcor()
    y_cor = snake.head.ycor()
    if x_cor > 295 or x_cor < -295 or y_cor > 295 or y_cor < -295:
        is_game_on = False


    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False

score_board.display_result()





screen.exitonclick()