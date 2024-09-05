
from turtle import Turtle, Screen

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")

segment_positions = [(0,0),(-20,0),(-40,0)]

for position in segment_positions:
    segment_1 = Turtle("square")
    segment_1.color("white")
    segment_1.goto(position)

screen.exitonclick()
