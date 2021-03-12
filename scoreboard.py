from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-220, 265)
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def scoring(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def start_over(self):
        self.penup()
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=FONT)