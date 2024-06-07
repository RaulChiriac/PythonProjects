from turtle import Screen
from character import Character
from score import Score
from obstacles import Obstacles
import time

screen = Screen()
screen.setup(600, 600)
screen.title('CrossyRoad')
screen.tracer(0)

char = Character()
obs = Obstacles()
score = Score()

screen.listen()
screen.onkey(char.get_up, 'Up')

gameStatus = True

while gameStatus:
    time.sleep(0.1)
    screen.update()

    obs.creat_obs()
    obs.move()

    for car in obs.obs:
        if car.distance(char) < 20:
            gameStatus = False
            score.game_over()

    if char.finish():
        char.go_start()
        obs.obs_speedup()
        score.level_up()
        if score.current_score == 5:
            score.game_over()
            gameStatus = False






screen.exitonclick()
