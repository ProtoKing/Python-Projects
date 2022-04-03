import pandas as pd
import numpy as np
import turtle
from turtle import Turtle

FONT = ("Calibri", 7, "normal")

screen = turtle.Screen()
screen.title("U.S States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
states = pd.read_csv("50_states.csv")
writer = Turtle()
writer.hideturtle()
guessed_states = []

game_is_on = True
while game_is_on:
    writer.penup()
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="What's another state's name?")

    if answer_state is None:
        game_is_on = False

    # Check if input matches the state
    if answer_state.title() in np.array(states.state):
        # Get hold of the coordinates of the state in df.
        guessed_states.append(answer_state.title())
        target_state = states[states["state"] == answer_state.title()]
        xcor = target_state.x
        ycor = target_state.y
        writer.goto(int(xcor), int(ycor))
        writer.write(answer_state.title())
        #
        # writer.goto(xcor,ycor)
        # writer.pendown()
        # writer.write(answer_state, font=FONT)
turtle.mainloop()