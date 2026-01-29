from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.highscore = 0
        self.score = 0
        self.penup()
        self.goto(-150,270)
        self.color("white")
        self.update_score()
        self.hideturtle()


    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}     High Score: {self.highscore}",align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def display_result(self):
        self.clear()
        self.write(f"Score: {self.score}",align="center", font=("Arial", 24, "normal"))
        self.goto(0,0)
        self.write(f"GAME OVER!",align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_score()