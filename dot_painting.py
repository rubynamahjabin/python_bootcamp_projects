import turtle
from turtle import Turtle,Screen
from random import choice

#List of RGB color tuples extracted from an image
color_list=[(245, 243, 238),(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50),
            (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86),
            (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
            (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
            (107, 127, 153), (176, 192, 208), (168, 99, 102)]

turtle.colormode(255)

def random_color():
    return choice(color_list)

tim=Turtle()
tim.speed("fastest") #speed set to fastest
tim.hideturtle() #hides the turtle icon
tim.penup() #to prevent drawing while moving

#Moving the turtle to starting position
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for _ in range(10):
    for _ in range(10):
        tim.dot(20,random_color())
        tim.forward(50)

    #after completing a row, moves up to begin a new row
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)

screen=Screen()
screen.exitonclick()