# Challenge 4
#Random walk

from turtle import Turtle, Screen
from random import choice

tim = Turtle()
tim.pensize(10) #Thick lines to clearly see
tim.speed(8) #Fast draw

colors = [
    'red', 'blue', 'green', 'orange', 'purple', 'yellow', 'cyan', 'magenta',
    'gold', 'pink', 'brown', 'black', 'gray', 'navy', 'turquoise', 'violet',
    'indigo', 'lime', 'maroon', 'olive', 'chocolate', 'coral', 'crimson', 'teal',
    'darkgreen', 'skyblue', 'deeppink', 'plum', 'salmon', 'slateblue'
]

direction=[0,90,180,270] #West,North,East,South

for _ in range(100):
    tim.color(choice(colors)) #Different colorful lines
    tim.forward(50)
    tim.setheading(choice(direction)) #Ensures the turtle walks in a fixed direction

screen = Screen()
screen.exitonclick()