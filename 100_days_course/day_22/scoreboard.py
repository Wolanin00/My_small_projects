from turtle import Turtle

FONT = ('Courier', 60, 'normal')
ALIGNMENT = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.refresh_scoreboard()

    def refresh_scoreboard(self):
        self.clear()
        self.goto(-80, 220)
        self.write(self.l_score, font=FONT, align=ALIGNMENT)
        self.goto(80, 220)
        self.write(self.r_score, font=FONT, align=ALIGNMENT)

    def l_point(self):
        self.l_score += 1
        self.refresh_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.refresh_scoreboard()



