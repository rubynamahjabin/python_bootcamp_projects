import turtle
from turtle import Turtle
from random import randint

tim = Turtle()
tim.speed("fastest")
turtle.colormode(255)

def random_color():
    r = randint(0,255)
    g = randint(0, 255)
    b = randint(0, 255)
    color=(r,g,b)
    return random

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(150)
        current_heading=tim.heading()
        tim.setheading(current_heading+size_of_gap)

draw_spirograph(5)

screen = turtle.Screen()
screen.exitonclick()