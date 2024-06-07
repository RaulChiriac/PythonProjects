from turtle import Turtle

UP = 20
DOWN = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def get_up(self):
        new_y = self.ycor() + UP
        self.goto(self.xcor(), new_y)

    def get_down(self):
        new_y = self.ycor() - DOWN
        self.goto(self.xcor(), new_y)
