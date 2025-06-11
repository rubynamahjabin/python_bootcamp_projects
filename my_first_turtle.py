from turtle import Turtle,Screen #imports necessary classes
timmy=Turtle() #creates a turtle object named timmy
timmy.shape("turtle") #sets its shape to look like a turtle
timmy.color('BlueViolet') #sets the color of the turtle to Blue Violet
timmy.forward(100) #moves the turtle forward 100 pixels (That is, draws a line)
print(timmy)
my_screen=Screen() #creates the drawing screen
print(my_screen.canvheight) #prints the height of that screen (default=300)
my_screen.exitonclick() #keeps the window open until you click on it