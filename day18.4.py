#Implementing random walk in turtle

from turtle import Turtle,Screen
import random
import turtle

timmy=Turtle()

colors=["yellow","red","black"]
i=0
directions=[0,90,180,270]
while(i<=50):
    turtle.hideturtle()
    timmy.pensize(10)
    timmy.color(random.choice(colors))
    timmy.forward(50)
    timmy.setheading(random.choice(directions))
    i+=1
screen= Screen()
screen.exitonclick()