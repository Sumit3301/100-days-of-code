# printing different shapes 
from turtle import Turtle,Screen
timmy=Turtle()
side=10
while(side>=1):

    for i in range(side):
        angle=360/side
        timmy.forward(100)
        timmy.right(angle)
    
    side-=1

screen= Screen()
screen.exitonclick()