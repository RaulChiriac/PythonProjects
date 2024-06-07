from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Georgia', 20, 'normal')

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0, 265)
        self.scorebord()

    def scorebord(self):
        self.write(f"Score: {self.score}",align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.scorebord()

    def gameover(self):
        self.color('white')
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

