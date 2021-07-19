import turtle
import colorgram
import random
from turtle import Turtle,Screen
rgb_colors=[]
turtle.colormode(255)
timmy=turtle.Turtle()
colors = colorgram.extract('damien.jpg', 30)
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    new_color=(r,g,b)
    rgb_colors.append(new_color)
print(rgb_colors)


timmy.dot(30,random.choice(rgb_colors))
timmy.forward(50)