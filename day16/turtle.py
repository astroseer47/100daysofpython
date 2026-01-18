# import turtle
# timmy = turtle.Turtle()

import prettytable_l

from turtle import Turtle, Screen

timmy = Turtle()

my_screen = Screen()
timmy.forward(100)
my_screen.exitonclick()

timmy.shape("turtle")
my_screen.bgcolor("white")
timmy.color("coral")