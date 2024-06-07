import random
from turtle import Turtle
from random import randint


STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
COLORS = ['red', 'orange', 'blue', 'green', 'yellow', 'purple']


class Obstacles:

    def __init__(self):
        self.obs = []
        self.obs_speed = STARTING_MOVE_DISTANCE

    def creat_obs(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_obs = Turtle()
            new_obs.shape('square')
            new_obs.penup()
            new_obs.shapesize(stretch_wid=1, stretch_len=2)
            new_obs.color(random.choice(COLORS))
            y_cor = randint(-250, 250)
            new_obs.goto(300, y_cor)
            self.obs.append(new_obs)

    def move(self):
        for car in self.obs:
            car.backward(self.obs_speed)

    def obs_speedup(self):
        self.obs_speed += 2




