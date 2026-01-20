from turtle import Turtle, Screen
import random
colors = ["red", "green", "blue", "yellow", "orange", "purple"]

turtles = []

y_start = 200
def get_initial_coordinates():
    global y_start
    y_start = y_start - 50
    return -180, y_start



def create_new_turtle():
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.color(colors[len(turtles)])
    co_ords = get_initial_coordinates()
    new_turtle.goto(co_ords)
    turtles.append(new_turtle)
    return new_turtle



screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color")
print(user_bet)

tim = create_new_turtle()
tom = create_new_turtle()
john = create_new_turtle()
jane = create_new_turtle()
don = create_new_turtle()
james = create_new_turtle()

is_race_on = False

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in turtles:
        if turtle.xcor() >= 220:
            is_race_on = False
            print(f"turtle {turtle.pencolor()} wins")
            if turtle.pencolor() == user_bet:
                print("Congrats! You win!")

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()