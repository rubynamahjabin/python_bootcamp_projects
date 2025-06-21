import turtle
from turtle import Turtle
from random import randint

tim = Turtle()
tim.speed("fastest")
turtle.colormode(255)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color=(r,g,b) #combines into a tuple
    return color

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color()) #sets the turtle's pen color to a random color
        tim.circle(150) #draw a circle with radius 150
        current_heading=tim.heading() #gets the current heading direction
        tim.setheading(current_heading+size_of_gap) #turns the turtle by size_of_gap degrees

draw_spirograph(5)

screen = turtle.Screen()
screen.exitonclick()
