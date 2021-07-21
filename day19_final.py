from hashlib import new
from turtle import Turtle,Screen, color, listen
import turtle
import random
colors=["red","green","blue","yellow"]
screen=Screen()
all_turtles=[]
y_pos=[-70,-40,-10,20]
bet=screen.textinput(title="Make your bet",prompt="Which turtle will win?Enter a color?:")
screen.setup(width=400,height=400)
for turtle_index in range(0,4):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-170,y=y_pos[turtle_index])
    all_turtles.append(new_turtle)

if bet:
    israce=True

while israce:
    for turtle in all_turtles:
        if
    for i in range(0,len(all_turtles)):
        random_increment=random.randint(0,10)
        turtle.forward()

screen.listen()
screen.exitonclick()