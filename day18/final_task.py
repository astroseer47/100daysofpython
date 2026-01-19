import random
import turtle as turtle_module

colors = ["DarkOrchid", "IndianRed", "DeepSkyBlue", "wheat"]

timmy = turtle_module.Turtle()


timmy.penup()
timmy.speed("fastest")
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(100)
timmy.setheading(0)

for dot_count in range(1, 101):
    timmy.color(random.choice(colors))
    timmy.dot(20, random.choice(colors))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)
#




screen = turtle_module.Screen()
screen.exitonclick()