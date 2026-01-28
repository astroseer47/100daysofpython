from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1


    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("Game Over!", align='center', font=('Arial', 24, 'normal'))

    def show_level(self):
        self.clear()
        self.goto(-250, 270)
        self.color("black")
        self.write(f"Level {self.level}", align='center', font=('Arial', 24, 'normal'))

    def level_up(self):
        self.level += 1
        self.show_level()