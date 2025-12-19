from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.score = 0
        file = open("high_score.txt")
        self.high_score = int(file.read())
        file.close()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", False, "center", ("Arial", 10, "normal"))

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            file = open("high_score.txt", mode="w")
            file.write(str(self.high_score))
            file.close()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
