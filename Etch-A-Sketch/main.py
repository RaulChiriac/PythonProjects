from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def moveForwords():
    tim.forward(10)

def moveBackwords():
    tim.backward(10)

def turnLeft():
    tim.left(10)

def turnRight():
    tim.right(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(moveForwords, 'w')
screen.onkey(moveBackwords, 's')
screen.onkey(turnLeft, 'a')
screen.onkey(turnRight, 'd')
screen.onkey(clear, 'c')
screen.exitonclick()
