from turtle import Turtle,Screen
timmy_the_turtle=Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
for i in range(4):
    timmy_the_turtle.forward(200)
    timmy_the_turtle.right(90)
screen=Screen()
screen.exitonclick()