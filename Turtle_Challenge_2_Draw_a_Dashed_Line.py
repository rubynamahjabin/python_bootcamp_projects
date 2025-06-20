# Challenge 2
# Draw a dashed line

from turtle import Turtle, Screen

tim = Turtle()

for i in range(10):
    tim.forward(10)  # draw
    tim.penup()  # no draw
    tim.forward(10)  # move forward while no draw, that is creating gap
    tim.pendown()  # draw

screen = Screen()
screen.exitonclick()  # keeps the turtle window open until a click