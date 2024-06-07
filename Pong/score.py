from turtle import Turtle

ALIGN = 'center'
FONT = ('Georgia', 80, 'normal')
WINFONT = ('Georgia', 20, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()
        self.winner = 'LEFT'

    def update_score(self):
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGN, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGN, font=FONT)

    def l_score_up(self):
        self.l_score += 1
        self.clear()
        self.update_score()

    def r_score_up(self):
        self.r_score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.color('white')
        self.goto(0, 0)
        self.write(f"GAME OVER THE WINNER IS {self.winner}", align=ALIGN, font=WINFONT)
