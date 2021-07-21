from turtle import Turtle,Screen, listen
import turtle

timmy1=Turtle()
timmy2=Turtle()
timmy3=Turtle()
timmy4=Turtle()
screen=Screen()
timmy1.color("red")
timmy2.color("blue")
timmy3.color("green")
timmy4.color("yellow")

turtle.setup(width=400,height=400)
timmy1.goto(x=-170,y=100)
timmy2.goto(x=-170,y=50)
timmy3.goto(x=-170,y=0)
timmy4.goto(x=-170,y=-50)


bet=screen.textinput(title="Make your bet",prompt="Which turtle will win?Enter a color?:")
def start_taste():
    


screen.listen()
screen.exitonclick()