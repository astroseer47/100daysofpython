import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("./50_states.csv")
all_states = data.state.to_list();

data_dict = data.to_dict('records')

states = []
while len(states) < 50:
    answer_state = screen.textinput(f"{len(states)}/50 States Guessed", "Enter a state")

    print(states)
    if answer_state in states:
        continue

    for stateEntry in data_dict:
        if stateEntry['state'].lower() == answer_state.lower():
            states.append(stateEntry['state'])
            text_turtle = turtle.Turtle()
            text_turtle.hideturtle()
            text_turtle.penup()
            text_turtle.goto(stateEntry['x'], stateEntry['y'])
            text_turtle.write(stateEntry['state'], font=("Arial", 6, "bold"))
            screen.update()



screen.exitonclick()