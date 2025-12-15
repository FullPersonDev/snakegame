from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.score = 0

    def create_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", False, "center", ("Arial", 10, "normal"))
