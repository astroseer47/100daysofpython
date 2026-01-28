import time
from turtle import Screen, Turtle

from day23.player import Player
from day23.car_manager import CarManager
from day23.scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
scoreboard.show_level()

screen.listen()


screen.onkey(player.up, "Up")


is_game_on = True

car_manager = CarManager()


while is_game_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            is_game_on = False

    # Detect a successful crossing
    if player.is_at_finish():
        player.goto_start()
        car_manager.level_up()
        scoreboard.level_up()

screen.exitonclick()