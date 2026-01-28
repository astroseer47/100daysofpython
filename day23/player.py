from turtle import Turtle

STARTING_POSITIONS = (0,-200)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.goto_start()


    def up(self):
        self.forward(MOVE_DISTANCE)


    def is_at_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        return False

    def goto_start(self):
        self.goto(STARTING_POSITIONS)
        self.setheading(90)