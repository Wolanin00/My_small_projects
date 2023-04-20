from turtle import Turtle

FONT_SCOREBOARD = ('Courier', 10, 'normal')
FONT_GAME_OVER = ('Courier', 20, 'normal')
ALIGNMENT = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.color('white')
        self.refresh_scoreboard()

    def refresh_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score}', font=FONT_SCOREBOARD, align=ALIGNMENT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f'Game over!', font=FONT_GAME_OVER, align=ALIGNMENT)

    def increase_score(self):
        self.score += 1
        self.refresh_scoreboard()

