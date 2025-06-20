# Challenge 3
# Draw different shapes

from turtle import Turtle, Screen
from random import choice

tim = Turtle()

colors = [
    'red', 'blue', 'green', 'orange', 'purple', 'yellow', 'cyan', 'magenta',
    'gold', 'pink', 'brown', 'black', 'gray', 'navy', 'turquoise', 'violet',
    'indigo', 'lime', 'maroon', 'olive', 'chocolate', 'coral', 'crimson', 'teal',
    'darkgreen', 'skyblue', 'deeppink', 'plum', 'salmon', 'slateblue'
]

for sides in range(3, 11):
    tim.color(choice(colors))  # choose a random color for each shape
    angle_of_shape = 360 / sides
    for _ in range(sides):
        tim.forward(100)
        tim.right(angle_of_shape)

screen = Screen()
screen.exitonclick()