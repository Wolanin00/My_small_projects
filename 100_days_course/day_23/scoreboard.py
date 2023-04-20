from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-290, 265)
        self.color('black')
        self.refresh_scoreboard()

    def refresh_scoreboard(self):
        self.clear()
        self.write(f'Level: {self.level}', font=FONT, align='left')

    def game_over(self):
        self.goto(0, 0)
        self.write(f'Game over!', font=FONT, align='center')

    def next_level(self):
        self.level += 1
        self.refresh_scoreboard()
