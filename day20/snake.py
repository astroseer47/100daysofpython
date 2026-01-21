from encodings.punycode import segregate
from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_block = Turtle("square")
            new_block.penup()
            new_block.color("white")
            new_block.goto(position)
            self.segments.append(new_block)

    def move(self):
        for block_index in range(len( self.segments) - 1, 0, -1):
            block = self.segments[block_index]
            last_block =  self.segments[block_index - 1]

            block.goto(last_block.xcor(), last_block.ycor())

        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
