import random
from turtle import Turtle, Screen

colors = ["DarkOrchid", "IndianRed", "DeepSkyBlue", "wheat"]
timmy = Turtle()

timmy.speed("fastest")
timmy.shape("turtle")
timmy.color("red")
# for _ in range(4):
#     timmy.forward(100)
#     timmy.left(90)
#
# timmy.clear()
#
# for _ in range(8):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()
#
# timmy.clear()
#
#
# def draw(num_sides):
#     for _ in range(num_sides):
#         angle = 360 / num_sides
#         timmy.forward(100)
#         timmy.right(angle)
#
# for shape_side_n in range (3,11):
#     timmy.color(random.choice(colors))
#     draw(shape_side_n)
#
# timmy.clear()
#
# directions = [0,90,180,270]
#
# timmy.pensize(15)
# for _ in range(100):
#     timmy.color(random.choice(colors))
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))

timmy.clear()

def draw_spirograph(size):
    for _ in range(int(360/size)):
        timmy.color(random.choice(colors))
        timmy.circle(100)
        current_heading = timmy.heading()
        timmy.setheading(current_heading + size)

draw_spirograph(5)



screen = Screen()
screen.exitonclick()
