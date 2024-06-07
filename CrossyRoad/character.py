from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH = 280


class Character(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.heading = (90, 0)
        self.left(90)
        self.penup()
        self.go_start()
    def get_up(self):
        self.forward(MOVE_DISTANCE)

    def finish(self):
        if self.ycor() > FINISH:
            return True
        else:
            return False

    def go_start(self):
        self.goto(STARTING_POSITION)

