from turtle import Turtle
from random import randint, choice
UP = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.shape('turtle')
        self.penup()
        self.hideturtle()
        self.sety(-270)
        self.setheading(90)
        self.showturtle()

    def move(self):
        self.sety(self.ycor() + UP)

    def start_over(self):
        self.sety(-270)