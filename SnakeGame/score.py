from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Georgia', 20, 'normal')

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as file:
            self.highScore = int(file.read())
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0, 265)
        self.score_bord()

    def score_bord(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highScore}",align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.score_bord()


    def reset(self):
        if self.score > self.highScore:
            self.highScore = self.score
            with open("data.txt", "w") as file:
                file.write(f"{self.highScore}")
        self.score = 0
        self.score_bord()


    # def gameover(self):
    #     self.color('white')
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

