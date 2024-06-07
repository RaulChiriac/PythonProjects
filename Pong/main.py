from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

scoreBoard = Score()

screen.listen()
screen.onkey(r_paddle.get_up, 'Up')
screen.onkey(r_paddle.get_down, 'Down')
screen.onkey(l_paddle.get_up, 'w')
screen.onkey(l_paddle.get_down, 's')

gameStatus = True
while gameStatus:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    if ball.xcor() > 370:
        ball.reset()
        scoreBoard.l_score_up()

    if ball.xcor() < -370:
        ball.reset()
        scoreBoard.r_score_up()

    if scoreBoard.l_score == 5:
        gameStatus = False
        scoreBoard.winner = 'LEFT'
        scoreBoard.game_over()

    if scoreBoard.r_score == 5:
        gameStatus = False
        scoreBoard.winner = 'RIGHT'
        scoreBoard.game_over()


screen.exitonclick()
