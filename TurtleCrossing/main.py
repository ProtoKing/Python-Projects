from turtle import Turtle
from turtle import Screen
from Player import Player
from Cars import Cars
from Scoreboard import Scoreboard
from random import randint, choice
import time

SPEED = 0.1
FINISH_LINE_Y = 290

# Set the Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.title('Classic Turtle Crossing Game,')
screen.tracer(0)

# Move the turtle Up
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, key="Up")

collection_of_cars = []
car_coordinates = []
loop_num = 0

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(SPEED)

    # Generate Random Cars every 6th loop
    if loop_num%6 ==0:
        cars = Cars()
        collection_of_cars.append(cars)
        car_coordinates.append((cars.xcor(), cars.ycor()))

    for cars in collection_of_cars:
        cars.forward(cars.speed)

    # Check if turtle collides with car
    for cars in collection_of_cars:
        if player.distance(cars.position()) <= 20:
            scoreboard.game_over()
            game_is_on = False

    # Top Edge Checker
    if player.ycor() >= FINISH_LINE_Y:
        for cars in collection_of_cars:
            player.goto(0, -280)
            scoreboard.score += 1
            scoreboard.update_scoreboard()
            cars.increase_speed()
    loop_num += 1
screen.exitonclick()