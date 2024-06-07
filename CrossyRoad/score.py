from turtle import Turtle
FONT = ('Courier', 24, 'normal')
WINFONT = ('Georgia', 24, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.current_score = 0
        self.update_score()

    def update_score(self):
        self.goto(-290, 260)
        self.write(f"LEVEL: {self.current_score}", font=FONT)

    def level_up(self):
        self.current_score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.color('black')
        self.goto(-160, 0)
        if self.current_score < 5:
            self.write("GAME OVER YOU LOSE", font=WINFONT)
        else:
            self.write("GAME OVER YOU WIN", font=WINFONT)


