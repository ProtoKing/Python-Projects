from turtle import Turtle
from random import randint, choice
COLORS =['blue', 'red', 'green', 'yellow', 'orange', 'violet', 'pink']
class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color(choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.setx(300)
        self.sety(randint(-230,250))
        self.setheading(180)
        self.speed = 5

    def start_moving(self):
        for new_xcor in range(300, -300, -10):
            self.goto(new_xcor, self.ycor())

    def increase_speed(self):
        self.speed += 5