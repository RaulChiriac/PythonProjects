import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Quiz")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv("50_states.csv")
stateList = data.state.to_list()
guessStates = []

while len(guessStates) < 50:

    answerState = screen.textinput(title=f"{len(guessStates)}/50 States Correct",
                                   prompt="What's another state's name:").title()
    if answerState == "Exit":
        missingStates = []
        for state in stateList:
            if state not in guessStates:
                missingStates.append(state)
        final = pandas.DataFrame(missingStates)
        final.to_csv("statesToLearn.csv")
        break
    if answerState in stateList:
        guessStates.append(answerState)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        stateCorrect = data[data.state == answerState]
        t.goto(float(stateCorrect.x), float(stateCorrect.y))
        t.write(stateCorrect.state.item())


screen.exitonclick()
