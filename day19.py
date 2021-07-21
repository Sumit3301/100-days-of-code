#Etch-A-Sketch app 

from turtle import Turtle,Screen, listen

timmy=Turtle()
screen=Screen()


def move_forward():
    timmy.forward(10)

def move_backwards():
    timmy.setheading(270)
def counter_clockwise():
    timmy.setheading(0)
def clockwise():
    timmy.setheading(180)

screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backwards)
screen.onkey(key="d",fun=counter_clockwise)
screen.onkey(key="a",fun=clockwise)
screen.exitonclick()


