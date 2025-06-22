#Turtle Race
from turtle import Turtle,Screen
from random import randint

screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")
colors=["red","orange","yellow","blue","violet","green","black"] #colors of the turtles racing
y_positions=[-120,-80,-40,0,40,80,120] #positions of the turtles at starting line
is_race_on=False
turtle_list=[]

#Turtles of different colors at the starting line
for turtle_index in range(7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-230, y_positions[turtle_index])
    turtle_list.append(new_turtle)

if user_bet:
    is_race_on=True #The race starts after user gives input

while is_race_on:

    for turtle in turtle_list:
        if turtle.xcor()>230:
            is_race_on = False #If turtle reaches finish line, stop the game
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance=randint(0,10) #Random speed
        turtle.forward(random_distance) #The turtle moves forward with this random speed

screen.exitonclick()